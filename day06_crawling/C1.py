from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.nate.com/")
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')
#result = soup.select("#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank")
result = soup.select("#olLiveIssueKeyword > li > a > span.txt_rank")
print(result)
print()

#print(result[0])
#print(result[0].string)
print(result[0].text)
print()

for top in result:
    print(top.text)