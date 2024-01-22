from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def scrape_wikipedia_with_selenium(url):
    # Set up Firefox options
    firefox_options = Options()
    firefox_options.headless = True  # Run Firefox in headless mode (without GUI)

    # Path to your geckodriver executable
    geckodriver_path = '/Users/mobilegalery/Downloads/geckodriver'

    # Set up Firefox webdriver
    service = FirefoxService(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=firefox_options)

    # Navigate to the Wikipedia page
    driver.get(url)

    # Wait for a few seconds to let the page load (you might need to adjust this time)
    driver.implicitly_wait(5)

    # Get the page source after waiting
    page_source = driver.page_source

    # Parse the HTML content of the page
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all paragraphs on the page
    paragraphs = soup.find_all('p')

    # Store paragraphs in a file
    with open('arabicData.txt', 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(paragraph.get_text() + '\n')

    # Close the webdriver
    driver.quit()

wikipedia_url = 'https://ar.wikipedia.org/wiki/تونس'
scrape_wikipedia_with_selenium(wikipedia_url)
