import urllib.parse
from urllib.parse import urlparse, urlunparse



def make_absolute_url(url, base_domain):
    """Convert single URL to absolute"""
    return urllib.parse.urljoin(base_domain, url)


def is_valid_url(url):
    """Check if single URL is valid HTTP/HTTPS"""
    parsed = urlparse(url)
    return parsed.scheme in ['http', 'https'] and parsed.netloc


def normalize_url(url):
    """Remove fragments from single URL"""
    parsed = urlparse(url)
    normalized = parsed._replace(fragment="")
    return urlunparse(normalized)


def is_same_domain(url, target_domain):
    """Check if URL belongs to the target domain"""
    parsed_url = urlparse(url)
    parsed_target = urlparse(target_domain)
    return parsed_url.netloc == parsed_target.netloc


def process_urls(urls, base_domain):
    processed_urls = []
    
    for url in urls:
        absolute_url = make_absolute_url(url, base_domain)
        
        if is_valid_url(absolute_url) and is_same_domain(absolute_url, base_domain):
            normalized_url = normalize_url(absolute_url)
            processed_urls.append(normalized_url)
    
    return processed_urls