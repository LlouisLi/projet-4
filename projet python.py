import subprocess
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import pandas as pd

#subprocess.run("gmail.com")

url = "https://mail.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

Gibaud = soup.find(attrs={'class':"zA zE"})
print(Gibaud)