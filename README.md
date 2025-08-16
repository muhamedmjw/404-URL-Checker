# 404 URL Checker

A Python tool that recursively crawls websites to find broken urls (404 errors). Perfect for identifying dead links that hurt user experience and SEO.

## Features

- **Recursive crawling**: Checks entire websites, not just single pages
- **Comprehensive detection**: Finds both broken internal links and broken pages
- **Domain filtering**: Only crawls links within the target domain
- **Clean reporting**: Lists all broken links with their HTTP status codes
- **Simple interface**: Just enter a URL and go

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool:
```bash
python main.py
```

Enter the website URL when prompted:
```
Enter the website URL to check: https://example.com
```

Example output:
```
Starting crawl of https://example.com...
Crawling: https://example.com
Found 15 links on this page
After processing: 8 valid links
broken on this page: 2
pages still to vist: 21
---
Crawling: https://example.com/about
Found 8 links on this page
After processing: 7 valid links
broken on this page: 0
pages still to vist: 19
...

=== CRAWL COMPLETE ===
Found 3 broken links:
1. https://example.com/old-page (Status: 404)
2. https://example.com/missing-file.pdf (Status: 404)
3. https://example.com/broken-link (Status: 404)
```

## How It Works

1. **Extract**: Parses HTML to find all `<a>` tag links
2. **Process**: Converts relative URLs to absolute, filters external domains
3. **Check**: Tests each URL for HTTP status codes
4. **Crawl**: Recursively visits all found pages on the domain
5. **Report**: Lists all URLs returning 404 or other error codes

## Project Structure

```
404-link-checker/
├── src/
│   ├── link_extractor.py    # HTML parsing with BeautifulSoup
│   ├── url_utils.py         # URL processing and validation
│   ├── http_checker.py      # HTTP status checking
│   └── crawler.py           # Recursive crawling logic
├── tests/
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Requirements

- Python 3.6+
- See `requirements.txt` for package dependencies

## Use Cases

- **Website maintenance**: Find broken links before users do
- **SEO optimization**: Fix 404s that hurt search rankings  
- **Quality assurance**: Validate links after site updates
- **Competitive analysis**: Check competitors' sites for issues