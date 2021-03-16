from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess
import time


def handler(event=None, context=None):
    subprocess.Popen(
        "udocker run -p 4444:4444 selenium/standalone-chrome".split(" "))
    time.sleep(30)
    options = {
        'command_executor': 'http://localhost:4444/wd/hub',
        'desired_capabilities': DesiredCapabilities.CHROME,
    }
    with webdriver.Remote(**options) as chrome:
        chrome.get("https://umihi.co/")
        return chrome.find_element_by_xpath("//html").text


if __name__ == '__main__':
    handler()
