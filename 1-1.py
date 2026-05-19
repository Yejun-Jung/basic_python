import requests

url = "https://www.daum.net/"

response = requests.get(url)

response.encoding="utp-8"

print(response.text)