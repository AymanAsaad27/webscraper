# Selenium Email Scraper: A Smart, Efficient, and Lightweight Web Scraper for Emails

This project is designed to simplify web scraping by automatically extracting email addresses (and optionally names) from web pages and saving them into an Excel file.

It utilizes **Selenium**, a powerful browser automation tool, to load and scrape dynamic content from websites effectively. With just a few lines of code, you can scrape emails from any webpage.

## Features

- Extracts email addresses from web pages efficiently.
- Optionally extracts associated names (based on HTML structure).
- Saves results in a clean, organized Excel file.
- Supports dynamic content scraping using Selenium.

## Installation

To use this project, make sure you have **Python 3.x** installed. Then, install the required libraries:

```bash
pip install selenium pandas openpyxl
```

Additionally, ensure that you have **ChromeDriver** installed and its path correctly set.

## How to Use

### 1. Setting Up

1. Clone this repository:
    ```bash
    git clone https://github.com/AymanAsaad27/webscraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd webscraper
    ```
3. Ensure you have the correct version of ChromeDriver for your browser and update the `driver_path` in the code.

### 2. Running the Scraper

Modify the script as necessary (e.g., changing the target URL) and run:

```bash
python selenium_email_scraper.py
```

The extracted emails (and optionally names) will be saved to an Excel file named `emails_with_names.xlsx`.

### Example Code

Here is a sample snippet from the project:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re
import pandas as pd

# Set up WebDriver
service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument("--headless")

# Navigate to the webpage
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.swpu.edu.cn/jdy/szdw/sss.htm")
time.sleep(3)

# Extract emails and save to Excel
page_source = driver.page_source
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page_source)
data = [{"Email": email} for email in emails]
df = pd.DataFrame(data)
df.to_excel("emails_with_names.xlsx", index=False)

# Quit WebDriver
driver.quit()
```
