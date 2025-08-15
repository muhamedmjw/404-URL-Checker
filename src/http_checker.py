import requests


def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        return {
            'url': url,
            'status_code': response.status_code,
            'is_broken': response.status_code >= 400
        }
    
    except requests.RequestException:
        return {
            'url': url,
            'status_code': None,
            'is_broken': True
        }


def process_url_status(urls):
    broken_urls = []

    for url in urls:
        result = check_url_status(url)
        if result['is_broken']:
            broken_urls.append(result)

    return broken_urls