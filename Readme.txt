# Web Scraper

This script periodically scrapes specified websites for a list of keywords and logs the findings. It's designed to be configurable and can handle modern JavaScript-based websites (Single Page Applications).

## Features

- **Periodic Scraping**: Runs automatically at regular intervals.
- **Configurable**: Target URLs and keywords can be easily modified in text files.
- **SPA Support**: Uses a real browser engine (via Selenium) to scrape dynamic content.
- **Daily Logs**: Saves results in a new log file each day (`log_YYYYMMDD.txt`).

## Requirements

The following packages are required. They are listed in `requirements.txt`.
- `selenium`
- `webdriver-manager`
- `schedule`

You will also need Google Chrome installed on the system where you run this script.

## Setup

1.  **Install Dependencies**:
    Open your terminal or command prompt and run the following command to install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

2.  **Configure URLs**:
    Edit the `urls.txt` file and add the full URLs of the websites you want to scrape, with one URL per line.
    Example:
    ```
    https://www.example.com/
    https://www.anothersite.org/
    ```

3.  **Configure Keywords**:
    Edit the `keywords.txt` file and add the keywords you want to search for, with one keyword per line.
    Example:
    ```
    Technology
    Finance
    Breaking News
    ```

## How to Run

Simply run the `main.py` script from your terminal:
```
python main.py
```
The script will start immediately, perform its first scrape, and then run once every hour. Scraping results will be saved in a file named `log_YYYYMMDD.txt` (e.g., `log_20231027.txt`).
