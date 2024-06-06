"""
class="tm-articles-list"
   article
   time datetime=
    h2
      a -> text

        id="post-content-body"
"""

import re
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


def get_headers():
    return Headers(browser="chrome", os="win").generate()


main_response = requests.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=get_headers())
main_html = main_response.text
main_soup = BeautifulSoup(main_html, "lxml")

list_cards = main_soup.find("main", class_="vacancy-serp-content")
cards = list_cards.find_all("div", class_="vacancy-card--H8LvOiOGPll0jZvYpxIF font-inter")

parsed_data = []

for card in cards:
    link = card.find("a", class_="bloko-link")
    link = link["href"]
    article_response = requests.get(link, headers=get_headers())
    article_soup = BeautifulSoup(article_response.text, "lxml")
    article_body_tag = article_soup.find("div", attrs={'data-qa': 'vacancy-description'})
    article_text = article_body_tag.text

    if re.search('Django', article_text) and re.search('Flask', article_text):
        salary = article_soup.find("span",
        class_="magritte-text___pbpft_3-0-4 magritte-text_style-primary___AQ7MW_3-0-4 magritte-text_typography-label-1-regular___pi3R-_3-0-4")
        name_company = article_soup.find("span",
        class_='bloko-header-section-2 bloko-header-section-2_lite')
        city = article_soup.find("p",
        attrs={'data-qa': 'vacancy-view-location'})
        print(link)
        parsed_data.append(
            {"link": link, "salary": salary.text, "name_company": name_company.text, "city": city.text}
        )

print(parsed_data)
print(len(parsed_data))
