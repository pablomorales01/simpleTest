
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def _driver():
    opts = ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return webdriver.Remote(command_executor=SELENIUM_REMOTE_URL, options=opts)

def test_homepage_and_interaction(tmp_path):
    driver = _driver()
    try:
        driver.get(BASE_URL)
        title = driver.find_element(By.ID, "title").text
        assert "Simple CI App" in title

        # Click a button and verify the counter increments
        inc_btn = driver.find_element(By.ID, "incBtn")
        counter = driver.find_element(By.ID, "counter")
        assert counter.text == "0"
        inc_btn.click()
        time.sleep(0.3)
        assert counter.text == "1"

        # Take a screenshot as artifact
        screenshot_path = os.getenv("ARTIFACT_SCREENSHOT", "artifacts/homepage.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
    finally:
        driver.quit()
