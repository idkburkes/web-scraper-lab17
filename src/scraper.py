import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = 0

    for anchor in soup.find_all('a', href=True):
        if anchor['href'] == '/wiki/Wikipedia:Citation_needed':
            res += 1
    return res

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = ''
    prefix = 'Citation needed for: \n'

    for anchor in soup.find_all('a', href=True):
        if anchor['href'] == '/wiki/Wikipedia:Citation_needed':
            parents = anchor.find_parents('p')
            for parent in parents:
                res += prefix + parent.text + '\n'

    return res


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Guam'

    count = get_citations_needed_count(url)
    print(count)

    report = get_citations_needed_report(url)
    print(report)