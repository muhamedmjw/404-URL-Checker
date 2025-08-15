from bs4 import BeautifulSoup
import requests


def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    anchors = soup.find_all('a')
    return [anchor['href'] for anchor in anchors if 'href' in anchor.attrs and anchor['href'].strip()]



if __name__ == "__main__":

    response = requests.get('https://learnxinyminutes.com/')
    html = response.text

    # with open('../test.html', 'r') as file:
    #     html = file.read()
    links = extract_links(html)
    
    print(links)