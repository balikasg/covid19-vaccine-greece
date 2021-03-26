import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging  
logging.basicConfig(level=logging.INFO)



logging.info('starting')
page = requests.get("https://emvolio.gov.gr/vaccinationtracker")
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
