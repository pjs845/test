from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=068270&page=1"
response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
source = response.text
#print(source)

soup = BeautifulSoup(source, 'lxml') #body > table.type2 > tbody > tr:nth-child(3) > td:nth-child(4) > span
span_today = soup.find('span', class_='tah p11')
#print(span_today)
#print(span_today.text)

td_pgRR = soup.find('td', class_='pgRR')
#print(td_pgRR)
#print(td_pgRR.text)
a_href = td_pgRR.a['href']
#print(a_href)
a_href_split_list = a_href.split("=")
print(a_href_split_list)
last_page = a_href_split_list[-1]
print(last_page)

import pandas as pd
df = pd.DataFrame()
base_url = "https://finance.naver.com/item/sise_day.nhn?code=068270"
#for page in range(1, int(last_page)+1):
for page in range(1, 10):
    url = "{}&page={}".format(base_url, page)
    response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html = pd.read_html(source, header=0)[0]
    #print(html)
    df = pd.concat([df, html])
#print(df.to_string())

df = df.dropna()
#print(df.to_string())
df = df.iloc[0:10]
#print(df.to_string())
df = df.sort_values(by='날짜')
print(df.to_string())

import matplotlib.pyplot as plt
plt.title("Celltrion Close")
plt.xticks(rotation=45)
plt.plot(df['날짜'], df['종가'], 'ro-')
plt.grid(color='gray', linestyle='--')
plt.show()