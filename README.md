# Web Scraper with Selenium

A simple Python script to scrape search results from a website using Selenium.

## Dependencies

- Python 3.x  
- Selenium (`pip install selenium`)  
- Chrome browser  
- ChromeDriver (matching your Chrome version) — download from https://chromedriver.chromium.org/downloads

## Usage

```python
scrape_with_selenium("https://yourwebsite.com", "your keyword", max_pages="Number of pages to search through")
