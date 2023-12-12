import requests
url="https://shibe.online/api/shibes?count=100"
response=requests.get(url)
data=response.json()
print(data)
