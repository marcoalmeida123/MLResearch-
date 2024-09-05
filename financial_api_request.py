import requests


#  replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=QQQ&interval=60min&apikey=AWS5XHAE2M1MSMUB'
r = requests.get(url)
data = r.json()

print(data) 