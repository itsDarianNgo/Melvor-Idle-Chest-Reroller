# src/browser_management/browser_init.py

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--disk-cache-size=1073741824")  # Set cache size to 1GB
    chrome_options.add_argument("user-agent=DN")  # Corrected user agent option
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--enable-gpu-rasterization")
    chrome_options.add_argument("--force-gpu-rasterization")
    chrome_options.add_argument("--ignore-gpu-blacklist")
    chrome_options.add_argument("--enable-accelerated-video-decode")
    chrome_options.add_argument("--max-tiles-for-interest-area=512")
    chrome_options.add_argument("--force-gpu-mem-available-mb=16384")
    chrome_options.add_argument("--renderer-process-limit=30")

    browser = uc.Chrome(options=chrome_options)
    return browser
