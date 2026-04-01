from __future__ import annotations

from dataclasses import asdict, dataclass
from pprint import pprint
import re
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag


BASE_URL = "https://static.valasztas.hu/dyn/pv14/szavossz/hu/oevker.html"
DETAIL_SUFFIX = "evkjkv.html"
CANDIDATE_TABLE_HEADERS = {"Sorszám", "A jelölt neve"}
REQUEST_TIMEOUT_SECONDS = 30
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; election-scraper/1.0)"}


@dataclass(frozen=True)
class OevkLink:
    code: str
    url: str


@dataclass(frozen=True)
class CandidateResult:
    number: str
    name: str
    nominating_organization: str
    votes: int
    elected: bool

    def as_output_dict(self) -> dict[str, Any]:
        return {
            "Sorszám": self.number,
            "A jelölt neve": self.name,
            "Jelölő szervezet": self.nominating_organization,
            "Kapott érvényes szavazat": self.votes,
            "Képviselő": self.elected,
        }


def get_soup(url: str, session: requests.Session | None = None) -> BeautifulSoup:
    client = session or requests
    response = client.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    response.encoding = "iso-8859-2"
    return BeautifulSoup(response.text, "html.parser")


def parse_index_links(index_soup: BeautifulSoup) -> list[OevkLink]:
    result_table = index_soup.find("table", border="1")
    if not isinstance(result_table, Tag):
        raise ValueError("Could not find the OEVK result table on the index page.")

    links: list[OevkLink] = []
    seen_urls: set[str] = set()

    for link in result_table.find_all(
        "a",
        href=lambda href: isinstance(href, str) and href.endswith(DETAIL_SUFFIX),
    ):
        href = link.get("href")
        if not isinstance(href, str):
            continue

        detail_url = urljoin(BASE_URL, href)
        if detail_url in seen_urls:
            continue

        seen_urls.add(detail_url)
        links.append(OevkLink(code=link.get_text(strip=True), url=detail_url))

    if not links:
        raise ValueError("No OEVK detail links were found on the index page.")

    return links


def extract_first_three_oevk_links(index_soup: BeautifulSoup) -> list[tuple[str, str]]:
    first_three_links = parse_index_links(index_soup)[:3]
    if len(first_three_links) < 3:
        raise ValueError("Found fewer than 3 OEVK links on the index page.")
    return [(link.code, link.url) for link in first_three_links]


def find_candidate_table(detail_soup: BeautifulSoup) -> Tag:
    for table in detail_soup.find_all("table"):
        header_cells = {
            cell.get_text(" ", strip=True)
            for cell in table.find_all("th")
        }
        if CANDIDATE_TABLE_HEADERS.issubset(header_cells):
            return table

    raise ValueError("Could not find the candidate results table on the detail page.")


def _extract_votes(text: str) -> int:
    digits_only = re.sub(r"\D", "", text)
    if not digits_only:
        raise ValueError(f"Could not parse vote count from {text!r}.")
    return int(digits_only)


def parse_candidate_row(row: Tag) -> CandidateResult | None:
    cells = row.find_all("td")
    if len(cells) < 6:
        return None

    return CandidateResult(
        number=cells[0].get_text(" ", strip=True),
        name=cells[1].get_text(" ", strip=True),
        nominating_organization=cells[2].get_text(" ", strip=True),
        votes=_extract_votes(cells[3].get_text(" ", strip=True)),
        elected=cells[5].find("img") is not None,
    )


def scrape_oevk(oevk_links: list[OevkLink], session: requests.Session | None = None) -> dict[str, list[CandidateResult]]:
    results: dict[str, list[CandidateResult]] = {}

    for oevk_link in oevk_links:
        detail_soup = get_soup(oevk_link.url, session=session)
        candidate_table = find_candidate_table(detail_soup)

        candidates: list[CandidateResult] = []
        for row in candidate_table.find_all("tr")[1:]:
            candidate = parse_candidate_row(row)
            if candidate is not None:
                candidates.append(candidate)

        results[oevk_link.code] = candidates

    return results


def scrape_first_three_oevk(session: requests.Session | None = None) -> dict[str, list[dict[str, Any]]]:
    index_soup = get_soup(BASE_URL, session=session)
    oevk_links = parse_index_links(index_soup)[:3]
    if len(oevk_links) < 3:
        raise ValueError("Found fewer than 3 OEVK links on the index page.")

    scraped_results = scrape_oevk(oevk_links, session=session)
    return {
        oevk_code: [candidate.as_output_dict() for candidate in candidates]
        for oevk_code, candidates in scraped_results.items()
    }


def main() -> None:
    pprint(scrape_first_three_oevk(), sort_dicts=False)


if __name__ == "__main__":
    main()
