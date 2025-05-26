from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time

def scrape_with_selenium(start_url, keyword, max_pages=30):
    options = Options()
    options.headless = True
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    visited = set()
    queue = deque([start_url])
    domain = urlparse(start_url).netloc

    print(f" Searching for '{keyword}' in pages from {start_url}\n")

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            driver.get(url)
            time.sleep(1)  
            html = driver.page_source
        except WebDriverException as e:
            print(f" Could not load {url}: {e}")
            continue

        if keyword.lower() in html.lower():
            print(f"Found '{keyword}' in: {url}")

        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('a', href=True):
            link = urljoin(url, tag['href'])
            if urlparse(link).netloc == domain and link not in visited:
                queue.append(link)

    driver.quit()
    print(f"\n Done! Checked {len(visited)} pages.")


scrape_with_selenium("https://www.nseindia.com", "holidays", max_pages=10)






