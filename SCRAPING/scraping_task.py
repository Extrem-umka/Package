import bs4
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

url = 'https://habr.com'
response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

KEYWORDS = [
    'PostgreSQL',
    'python',
    'android',
    'telegram'
]


articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.strip() for hub in hubs]
    title = article.find("h2").find("span").text
    # print(title)
    date = article.find('time').text
    # print(date)
    href = article.find(class_='tm-article-snippet__title-link').attrs["href"]
    # print(href)
    full_href = f"{url}{href}"
    # print(full_href)
    for hub in hubs:
        if hub in KEYWORDS:
            print(f'Название статьи: {title}\nДата выпуска: {date}\nСсылка на статью: {full_href}')




