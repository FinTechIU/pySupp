from bs4 import BeautifulSoup
import requests

id = 97210
url = "https://pricing.grixisutils.site/"

soup = BeautifulSoup(requests.get(url, params={'id': id}).text, 'lxml')

#print(soup.prettify())

#print(soup.head)
#print(soup.title)

price_table = soup.find('span', class_='price-results-div').table

'''
for row in price_table.find_all('tr'):
    print(row)
    ents = row.find_all('td')
    print(ents[0].string, ents[1].string.split(chr(0xA0))[0])
'''
#'''
