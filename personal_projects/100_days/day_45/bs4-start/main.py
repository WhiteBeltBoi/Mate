from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    website = file.read()



soup = BeautifulSoup(website, 'html.parser')
# print(soup.title.string)
all_anchor_tags = soup.find_all(name = "a")

# print([tag.getText() for tag in all_anchor_tags])
# print([tag.get("href") for tag in all_anchor_tags])
heading = soup.find(name = "h1")
print(heading)