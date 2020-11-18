#scraper_currency.py
import requests
from bs4 import BeautifulSoup
import csv



headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

url = 'https://www.countries-ofthe-world.com/world-currencies.html'
response = requests.get(url , headers = headers)
#print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
#title = soup.find(id="firstHeading")
#print(title.string)
My_table = soup.find('table',{'class':'codes'})
#header = soup.find('th' , {'class': "headerSort"})
#links = My_table.findAll('a')
rows = My_table.find_all('tr')
titles = My_table.find_all('th')
#print((titles))



with open ('currency_list.csv','w') as file:
    writer=csv.writer(file)
    #header_row= []
    # for title in titles :
    #     header_row.append([val.text.encode('utf8').rstrip() for val in title.find_all(['td', 'th'])])
    #     # print(title)
    #     # #t_cols=title.find_all('th')
    #     # t_cols=[x.text.strip() for x in title]
    #     header_row.append(title)
    # writer.writerow(header_row)

    for row in rows:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        #print (cols)
        writer.writerow(cols)
print('... done ')
