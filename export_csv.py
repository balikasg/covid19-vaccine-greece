import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging  
logging.basicConfig(level=logging.INFO)



logging.info('starting')
headers = {
           "referer": "https://emvolio.gov.gr/vaccinationtracker",
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'gzip, deflate',
           'accept-language': 'en-US,en;q=0.9',
           'sec-ch-ua': '"Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"',
           'sec-ch-ua-mobile': '?0',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

page = requests.get("https://emvolio.gov.gr/vaccinationtracker", headers=headers)
logging.info(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
df = soup.find_all('table', class_='table-striped table table-hover')
df = pd.read_html(df[0].prettify())
print(len(df))
df = df[0]


import datetime
dt = datetime.datetime.today()
fname = "data/{:04d}_{:02d}_{:02d}_{:02d}_{:02d}.csv".format(dt.year, dt.month, dt.day, dt.hour, dt.minute)
print(fname)
df.to_csv(fname, index=False, header=True)
