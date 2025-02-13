import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# Base URL of the website to crawl
base_url = "http://thedigitz.com/"  # Replace with your website's URL
visited_pages = set()  # Keep track of visited pages
broken_images = []  # List to store broken image URLs


def is_valid_url(url, base_url):
    """Check if a URL is valid and belongs to the same domain."""
    parsed = urlparse(url)
    return parsed.netloc == urlparse(base_url).netloc and parsed.scheme in ("http", "https")


def crawl_page(url):
    """Crawl a single page to find broken images."""
    if url in visited_pages:  # Skip already visited pages
        return
    visited_pages.add(url)  # Mark the page as visited

    try:
        driver.get(url)  # Load the page in the browser
    except Exception as e:
        print(f"Error loading page: {url} | Error: {e}")
        return

    # Find all images on the page
    images = driver.find_elements(By.TAG_NAME, "img")
    for image in images:
        img_url = image.get_attribute("src")
        if img_url:
            # Ensure the image URL is absolute
            full_img_url = urljoin(base_url, img_url)
            try:
                response = requests.get(full_img_url, timeout=5)
                if response.status_code != 200:
                    broken_images.append(full_img_url)
                    print(f"Broken image found: {full_img_url}")
            except requests.exceptions.RequestException:
                broken_images.append(full_img_url)
                print(f"Error checking image: {full_img_url}")

    # Find all internal links on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        if href and is_valid_url(href, base_url):
            crawl_page(href)  # Recursively crawl the linked page


# Start crawling from the base URL
crawl_page(base_url)

# Print results
print("\nCrawling complete!")
if broken_images:
    print("List of broken images:")
    for img in broken_images:
        print(img)
else:
    print("No broken images found.")

# Close the browser
driver.quit()
