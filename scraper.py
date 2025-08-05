import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape(url: str, keywords: list[str]) -> dict:
    """
    Scrapes a given URL for a list of keywords.

    Args:
        url: The URL to scrape.
        keywords: A list of keywords to search for.

    Returns:
        A dictionary containing the scraping results.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use webdriver-manager to automatically handle the driver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    results = {
        "url": url,
        "found_keywords": [],
        "timestamp": datetime.datetime.now().isoformat()
    }

    try:
        driver.get(url)
        # Wait for the body tag to be present, a simple way to wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Get the entire page's text content
        page_text = driver.find_element(By.TAG_NAME, "body").text

        for keyword in keywords:
            if keyword in page_text:
                results["found_keywords"].append(keyword)

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
    finally:
        driver.quit()

    return results

if __name__ == '__main__':
    # Example usage for testing
    test_url = "https://www.yahoo.co.jp/"
    test_keywords = ["ニュース", "天気", "経済", "スポーツ"]
    scrape_results = scrape(test_url, test_keywords)
    print(scrape_results)
