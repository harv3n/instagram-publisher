#coding=utf-8
import time
import sys
import os
import shutil
import errno
import configparser
import boto3
import pytz
import random
import urllib.request
import socket
import urllib.error
import csv
from botocore.exceptions import ClientError
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Main functions
def instagram():
    chrome_options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    chrome_options.add_argument('user-agent={0}'.format(user_agent))
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')  

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get('https://www.instagram.com')

    time.sleep(2)

    fb_login = driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF')
    fb_login.click()

    time.sleep(10)

if __name__ == '__main__':
    instagram()