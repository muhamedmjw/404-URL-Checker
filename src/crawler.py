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
            print(f"Crawling: {current_page}")
            try:
                response = requests.get(current_page, timeout=10)
                if response.status_code >= 400:  # Page itself is broken
                    broken_urls.append({
                        'url': current_page,
                        'status_code': response.status_code,
                        'is_broken': True
                    })
                html = response.text
            except requests.RequestException:
                continue  # Skip this page if it fails

            urls = extract_urls(html)
            clean_urls = process_urls(urls, base_domain)
            page_broken_urls = process_url_status(clean_urls)

            broken_urls.extend(page_broken_urls)
            pages_to_visit.extend(clean_urls)
            pages_already_visited.append(current_page)

            print(f"  -> Found {len(urls)} raw links")
            print(f"  -> After processing: {len(clean_urls)} valid links") 
            print(f"  -> Broken on this page: {len(page_broken_urls)}")
            print(f"  -> Pages still to visit: {len(pages_to_visit)}")
            print("---")

            max_pages = 10  # Stop after n pages
            if len(pages_already_visited) >= max_pages:
                break

    return broken_urls
