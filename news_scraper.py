from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_bloomberg_news():
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.bloomberg.com/markets")

    # Print the full page source to debug
    print(driver.page_source[:1000])  # Print first 1000 characters of HTML
    
    driver.quit()

get_bloomberg_news()
