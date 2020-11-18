
import pandas as pd

import requests
import io
import datetime
#url = 'https://api.exchangeratesapi.io/latest/'
url='https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-12-31'
r = requests.get(url)



# response = requests.get(url )
# #print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.pretify())
filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
save_path = 'exchange_rate_years' +  filename1 + '.txt'
open(save_path, 'wb').write(r.content)

#rawData = pd.read_csv(io.StringIO(r.content.decode('utf-8')))
#rawData
#rawData.to_csv('temp.csv')

