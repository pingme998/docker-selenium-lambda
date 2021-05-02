from selenium import webdriver


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/bin/headless-chromium"
    event = event if event is not None else {}
    args = event.get('args', [
        '--headless',
        '--no-sandbox',
        "--disable-gpu",
        "--window-size=1280x1696",
        "--single-process",
        "--disable-dev-shm-usage",
    ])
    for arg in args:
        options.add_argument(arg)
    chrome = webdriver.Chrome("/opt/bin/chromedriver",
                              options=options)
    chrome.get("https://umihi.co/")
    return chrome.find_element_by_xpath("//html").text
