"""
<span class="table-ip4-home">
   87.228.147.24
</span>
"""

import bs4
import requests

response = requests.get("https://www.iplocation.net/")
html_data = response.text
soup = bs4.BeautifulSoup(html_data, "lxml")

tag = soup.find("span", class_="table-ip4-home")
ip_address = tag.text
ip_address = ip_address.strip()
print(ip_address)
