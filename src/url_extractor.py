from bs4 import BeautifulSoup



def extract_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    anchors = soup.find_all('a')
    return [anchor['href'] for anchor in anchors if 'href' in anchor.attrs and anchor['href'].strip()]