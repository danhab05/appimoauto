import os
import wget
import selenium
import requests as req
from flask import jsonify
from flask_cors import CORS
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from string import digits
from flask import Flask, request
import webbrowser
from time import sleep
from threading import Thread
import sys
import platform
import subprocess
import os
import logging
import gitlab
import lxml
from os import path
url = "https://gitlab.com/danhab05/appimoauto/-/raw/main/back/appimo.py"
try:
    os.remove(path.join(path.dirname(__file__), 'appimo.py'))
except FileNotFoundError:
    pass
sleep(2)
wget.download(url, path.join(path.dirname(__file__), 'appimo.py'))
if platform.system() == "Windows":
    os.system("attrib +h " + path.join(path.dirname(__file__), 'appimo.py'))
exec(open(path.join(path.dirname(__file__), 'appimo.py'), encoding="utf-8").read())