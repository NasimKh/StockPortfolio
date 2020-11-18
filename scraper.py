
import requests
from bs4 import BeautifulSoup
import csv

response = requests.get(
    url="https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report",
)
#print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
#title = soup.find(id="firstHeading")
#print(title.string)
My_table = soup.find('table',{'class':'wikitable sortable'})
#header = soup.find('th' , {'class': "headerSort"})
#links = My_table.findAll('a')
rows = My_table.find_all('tr')
titles = My_table.find_all('th')




with open ('wiki_happiness_score.csv','w') as file:
    writer=csv.writer(file)
    header_row= []
    for title in titles :
        t_cols=title.find_all('abbr')
        t_cols=[x.text.strip() for x in t_cols]
        header_row.append(t_cols)
    writer.writerow(header_row)

    for row in rows:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        #print (cols)
        writer.writerow(cols)

