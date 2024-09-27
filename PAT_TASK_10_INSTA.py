"""
Python Selenium - Extracting Followers and Following from Instagram using Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class InstagramFollowerExtractor:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)  # Wait for the page to load completely

    def shutdown(self):
        self.driver.quit()

    # Extract followers and following count
    def extract_counts(self):
        # Use XPATH to extract followers and following counts
        followers = self.driver.find_element(by=By.XPATH, value="//a[contains(@href,'followers')]//span").text
        following = self.driver.find_element(by=By.XPATH, value="//a[contains(@href,'following')]//span").text

        return followers, following


if __name__ == "__main__":
    url = "https://www.instagram.com/guviofficial/"
    extractor = InstagramFollowerExtractor(url)
    extractor.start()
    
    # Extract and display followers and following counts
    followers, following = extractor.extract_counts()
    print("Total Followers:", followers)
    print("Total Following:", following)
    
    extractor.shutdown()
