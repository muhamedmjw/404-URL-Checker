import requests
from src.link_extractor import extract_links
from src.url_utils import process_urls
from src.http_checker import process_url_status



def get_domain_from_user():
    """Get target domain from user input"""
    domain = input("Enter the website URL to check: ").strip()
    
    # Add basic validation
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain
    
    return domain


def main():
    base_domain = get_domain_from_user()
    
    try:
        response = requests.get(base_domain, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Link Checker Bot)'
        })
        response.raise_for_status()  # Raises exception for 4xx/5xx status codes
        html = response.text
    except requests.RequestException as e:
        print(f"Error fetching {base_domain}: {e}")
        return
    
    raw_urls = extract_links(html)
    clean_urls = process_urls(raw_urls, base_domain)
    broken_url = process_url_status(clean_urls)
    
    

if __name__ == "__main__":
    main()