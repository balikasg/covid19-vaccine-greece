import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging  
logging.basicConfig(level=logging.INFO)



logging.info('starting')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
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
