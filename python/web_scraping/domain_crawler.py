import csv
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


class DomainCrawler:

    def __init__(self, starting_url, output_filename='output.csv', max_pages=25):
        self.starting_url = starting_url
        self.parsed_starting_url = urlparse(starting_url)
        self.visited_urls = []
        self.data = {}
        self.max_pages = max_pages
        self.processed_pages = 0

        try:
            self.csv_file = csv.writer(open(output_filename, 'w'), delimiter=',')
        except:
            print('[-] Error loading CSV file for writing.')
        self.csv_file.writerow(['Title', 'Href'])

    def process_page(self, href):
        if self.processed_pages >= self.max_pages:
            return

        url = urlparse(href)
        if url.netloc == "":
            href = self.parsed_starting_url.scheme + '://' +\
                   self.parsed_starting_url.netloc +\
                   href

        if href not in self.visited_urls:
            self.visited_urls.append(href)
        else:
            return

        print('[*] Processing %s' % href)
        self.processed_pages += 1

        try:
            response = requests.get(href)
        except:
            return

        soup = BeautifulSoup(response.text)
        self.csv_file.writerow([soup.title.string, href])

        for a in soup.find_all('a'):
            if self.does_url_stay_onsite(a.get('href')):
                self.process_page(a.get('href'))

    def does_url_stay_onsite(self, href):
        url = urlparse(href)
        if url.netloc == "" or url.netloc == self.parsed_starting_url.netloc:
            return True

    def start(self):

        self.process_page(self.starting_url)

        print('[+] Complete!')


if __name__ == '__main__':
    crawler = DomainCrawler('https://www.devdungeon.com')
    crawler.start()

