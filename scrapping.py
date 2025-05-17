from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.climatempo.com.br")
html = response.content
soup = BeautifulSoup(html, 'html.parser')

temperatura = soup.find("span", {
    "class": "-text -bold -gray-dark-2 -font-55 _margin-l-15",
    "id": "current-weather-temperature"
})


print(response.status_code)
#print(soup.prettify())
print(temperatura.string)