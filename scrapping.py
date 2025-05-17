from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


driver.get("https://www.transfermarkt.pt/statistik/weltrangliste")


time.sleep(5)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


ranking = soup.find("main",id_="tm-main")

print(ranking.text.strip())

driver.quit()
