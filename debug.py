from selenium import webdriver
import os
import subprocess
from test import handler


def debug(event=None, context=None):
    # text = handler()
    text = "\n".join([
        subprocess.run([
            "google-chrome",
            "--user-data-dir=/tmp/home/user-data",
            "--no-sandbox",
            "--headless",
            "--disable-gpu",
            "--dump-dom",
            "--single-process",
            "--disable-dev-shm-usage",
            "https://example.com"
        ], capture_output=True, text=True).stdout,
    ])
    # try:
    # except Exception as e:
    #     text = [
    #         str(e),
    #         *subprocess.run(
    #             ['find', '/tmp', '-print'], capture_output=True, text=True).stdout.split("\n"),
    #         subprocess.run(
    #             ['cat', '/tmp/home/user-data/Default/chrome_debug.log'], capture_output=True, text=True).stdout.split("\n"),
    # s    ]
    return text


if __name__ == '__main__':
    print(debug())
