import requests

url = "https://www.amazon.com"
data = requests.get(url)
if data.status_code == 200:
    print(data.text)
else:
    print("permission denied")