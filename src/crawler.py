import requests
from src.url_extractor import extract_urls
from src.url_utils import process_urls
from src.http_checker import process_url_status


def crawl_website(base_domain):
    pages_to_visit = [base_domain]
    pages_already_visited = []
    broken_urls = []

    while pages_to_visit:
        current_page = pages_to_visit.pop(0)

        if current_page not in pages_already_visited:
            try:
                html = requests.get(current_page, timeout=10).text
            except requests.RequestException:
                continue  # Skip this page if it fails

            urls = extract_urls(html)
            clean_urls = process_urls(urls, base_domain)
            page_roken_urls = process_url_status(clean_urls)
            
            broken_urls.extend(page_roken_urls)
            pages_to_visit.append(clean_urls)
            pages_already_visited.append(current_page)

    return broken_urls
