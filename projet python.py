#import subprocess
import requests
import urllib.request #permettent de faire des requetes
from bs4 import BeautifulSoup #rendre pages accessibles
import pandas as pd #pour mettre l'objet dans un table
from selenium import webdriver #permettra de tansformer le 
#code dans "inspecter de la page en html"
from time import sleep #repos 

def connection():
    url = "https://mail.google.com/mail/u/0/#sent"
    css_selector = ".zA yO" #id de la ligne du tableau avec l'adresse mail

    wd_path = "PROJET ER/chromedriver" #chromedriver: pouvoir interagir avec la page google

    wdriver = webdriver.Chrome(executable_path = wd_path) 

    wdriver.get(url)
    #subprocess.run("gmail.com")
    return wdriver

url = "https://mail.google.com/mail/u/0/#sent"
response = requests.get(connection)
soup = BeautifulSoup(response.text,"html.parser")

Gibaud = soup.findAll("td")
for i in Gibaud:
    print(i["class"])