from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re
import pandas as pd

# Path to your chromedriver
driver_path = r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Set up the Chrome service
service = Service(driver_path)

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for better performance
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode
chrome_options.add_argument("--no-sandbox")  # Disable sandbox for better compatibility

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the target webpage
url = "https://www.swpu.edu.cn/jdy/szdw/sss.htm"

# Navigate to the page
driver.get(url)

# Wait for the page to load completely
time.sleep(5)  # Adjust this delay if the website takes more time to load

# Get the page source after it's fully loaded
page_source = driver.page_source

# Use regex to extract all email addresses from the page source
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page_source)

# Log the extracted email addresses
print(f"Extracted Emails: {emails}")

# Prepare data for Excel (each email on a new row)
data = [{"Email": email} for email in emails]

# Write to an Excel file
df = pd.DataFrame(data)
output_file = "emails.xlsx"
df.to_excel(output_file, index=False)

print(f"Email addresses have been successfully saved to {output_file}")

# Quit the WebDriver
driver.quit()
