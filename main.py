import schedule
import time
import datetime
from scraper import scrape

def read_items_from_file(filename: str) -> list[str]:
    """Reads items from a file, one per line."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def write_log(result: dict):
    """Writes the scraping result to a log file named with the current date."""
    today = datetime.datetime.now().strftime("%Y%m%d")
    log_filename = f"log_{today}.txt"

    with open(log_filename, 'a', encoding='utf-8') as f:
        f.write(f"Timestamp: {result['timestamp']}\n")
        f.write(f"URL: {result['url']}\n")
        f.write(f"Found Keywords: {', '.join(result['found_keywords']) if result['found_keywords'] else 'None'}\n")
        f.write("-" * 20 + "\n")

def job():
    """The main scraping job."""
    print("Starting scraping job...")
    urls = read_items_from_file("urls.txt")
    keywords = read_items_from_file("keywords.txt")

    if not urls or not keywords:
        print("No URLs or keywords to process. Exiting job.")
        return

    for url in urls:
        print(f"Scraping {url}...")
        result = scrape(url, keywords)
        write_log(result)
        print(f"Finished scraping {url}. Results logged.")

    print("Scraping job finished.")

def main():
    """Runs the scheduler."""
    print("Scheduler started. The job will run every hour.")
    # For demonstration, let's schedule it every hour.
    # You can change this to `schedule.every().day.at("10:30")` or other intervals.
    schedule.every().hour.do(job)

    # Run the job once immediately at the start
    job()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
