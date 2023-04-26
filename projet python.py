import subprocess
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

#subprocess.run("gmail.com")

url = "https://accounts.google.com/AccountChooser/signinchooser"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(soup)
for i in soup:
    print (i)