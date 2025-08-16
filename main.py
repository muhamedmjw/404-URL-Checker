import requests
from src.url_extractor import extract_urls
from src.url_utils import process_urls
from src.http_checker import process_url_status
from src.crawler import crawl_website


def get_domain_from_user():
    """Get target domain from user input"""
    domain = input("Enter the website URL to check: ").strip()
    
    # Add basic validation
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain
    
    return domain


def main():
    base_domain = get_domain_from_user()
    
    print(f"Starting crawl of {base_domain}...")
    broken_links = crawl_website(base_domain)
    
    # Remove duplicates by URL
    unique_broken = []
    seen_urls = set()
    
    for link in broken_links:
        if link['url'] not in seen_urls:
            unique_broken.append(link)
            seen_urls.add(link['url'])
    
    print(f"Found {len(unique_broken)} unique broken links:")
    for i, link in enumerate(unique_broken, 1):
        print(f"{i}. {link['url']} (Status: {link['status_code']})")



if __name__ == "__main__":
    main()