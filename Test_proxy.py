import requests
from bs4 import BeautifulSoup

proxies = {
    "https": "http://C2q16j:QZJsqX@212.81.37.150:9965"
                }

response = requests.get('https://ipinfo.io', proxies=proxies)
    
print(response.text()   )