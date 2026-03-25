from __future__ import annotations

from pprint import pprint
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


# This is the index page that lists every OEVK constituency result page.
BASE_URL = "https://static.valasztas.hu/dyn/pv14/szavossz/hu/oevker.html"

# Some sites behave better when the request looks like it comes from a browser.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; election-scraper/1.0)"
}


def get_soup(url: str) -> BeautifulSoup:
    # 1. Download the page HTML from the given URL.
    response = requests.get(url, headers=HEADERS, timeout=30)

    # 2. Stop immediately if the server returned an error like 404 or 500.
    response.raise_for_status()

    # 3. This site uses ISO-8859-2 encoding, not UTF-8.
    # Without this line, Hungarian characters can look broken.
    response.encoding = "iso-8859-2"

    # 4. Convert the HTML text into a BeautifulSoup object so we can search it.
    return BeautifulSoup(response.text, "html.parser")


def extract_first_three_oevk_links(index_soup: BeautifulSoup) -> list[tuple[str, str]]:
    # The main results page contains multiple tables. We want the first border="1"
    # table, which is the one that lists the OEVK rows and links.
    result_table = index_soup.find("table", border="1")
    if result_table is None:
        raise ValueError("Could not find the OEVK result table on the index page.")

    links: list[tuple[str, str]] = []
    seen_urls: set[str] = set()

    # We scan every link in that table and keep only those that point to
    # constituency result pages ending in "evkjkv.html".
    for link in result_table.find_all("a", href=lambda href: isinstance(href, str) and href.endswith("evkjkv.html")):
        # Convert relative links like "M01/E01/evkjkv.html" into full URLs.
        detail_url = urljoin(BASE_URL, link["href"])

        # Skip duplicates. The table structure can cause the same OEVK link
        # to appear more than once while traversing the HTML.
        if detail_url in seen_urls:
            continue

        seen_urls.add(detail_url)
        oevk_code = link.get_text(strip=True)
        links.append((oevk_code, detail_url))

        # The task only asks for the first 3 OEVK links.
        if len(links) == 3:
            break

    if len(links) < 3:
        raise ValueError("Found fewer than 3 OEVK links on the index page.")

    return links


def find_candidate_table(detail_soup: BeautifulSoup) -> BeautifulSoup:
    # Each constituency detail page has several tables.
    # We identify the candidate table by looking for header names we expect.
    for table in detail_soup.find_all("table"):
        header_cells = [cell.get_text(" ", strip=True) for cell in table.find_all("th")]
        if "Sorszám" in header_cells and "A jelölt neve" in header_cells:
            return table

    raise ValueError("Could not find the candidate results table on the detail page.")


def parse_candidate_row(row) -> dict[str, object] | None:
    cells = row.find_all("td")

    # Ignore header rows or malformed rows that do not contain candidate data.
    if len(cells) < 6:
        return None

    # Vote counts contain spacing characters, sometimes non-breaking spaces.
    # Keeping only digits gives us a clean numeric string like "21503".
    votes = re.sub(r"\D", "", cells[3].get_text(" ", strip=True))

    return {
        "Sorszám": cells[0].get_text(" ", strip=True),
        "A jelölt neve": cells[1].get_text(" ", strip=True),
        "Jelölő szervezet": cells[2].get_text(" ", strip=True),
        "Kapott érvényes szavazat": votes,
        # On this site, the elected representative is shown with a checkmark image.
        # If the image exists in the cell, we store True, otherwise False.
        "Képviselő": cells[5].find("img") is not None,
    }


def scrape_first_three_oevk() -> dict[str, list[dict[str, object]]]:
    # Step 1: load the main page that lists all constituencies.
    index_soup = get_soup(BASE_URL)

    # Step 2: collect the first 3 constituency result links from that page.
    oevk_links = extract_first_three_oevk_links(index_soup)

    results: dict[str, list[dict[str, object]]] = {}
    for oevk_code, detail_url in oevk_links:
        # Step 3: open each constituency page.
        detail_soup = get_soup(detail_url)

        # Step 4: locate the table that contains the candidate results.
        candidate_table = find_candidate_table(detail_soup)

        candidates: list[dict[str, object]] = []

        # The first <tr> is the header row, so we skip it with [1:].
        for row in candidate_table.find_all("tr")[1:]:
            candidate = parse_candidate_row(row)
            if candidate is not None:
                candidates.append(candidate)

        # Store all candidates under the OEVK code, for example "01", "02", "03".
        results[oevk_code] = candidates

    return results


if __name__ == "__main__":
    # pprint prints nested dictionaries/lists in a readable way for debugging.
    pprint(scrape_first_three_oevk(), sort_dicts=False)
