from .config import settings
import requests
from bs4 import BeautifulSoup

class DouBan:

    def __init__(self, keywords):
        self.keywords = keywords

    def fetch(self):
        url = settings.DOUBAN_SEARCH + self.keywords
        try:
            response = requests.get(url, headers=settings.CRAWLER_HEADERS)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                detail_url = self.parse_link(response.text)
                spoiler_text = self.fetch_detail(detail_url)
                return spoiler_text
            else:
                return None
        except Exception as e:
            print(e)

    def parse_link(self, content):

        soup = BeautifulSoup(content, settings.PARSER)
        a_tag = soup.find_all('h3')[0].a
        return a_tag['href']

    def fetch_detail(self, url):
        try:
            response = requests.get(url, headers=settings.CRAWLER_HEADERS)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, settings.PARSER)
                init_short_comment_seq = soup.find_all('span', attrs={'class': 'short'})
                short_comment_seq = [s.string for s in init_short_comment_seq]
                return ''.join(short_comment_seq)
            else:
                return None
        except Exception as e:
            print(e)