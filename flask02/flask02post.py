import requests
url = "http://192.168.209.128:5000/user"
payload = {"name":"riverhsu", "age":"54"}
response = requests.post(url, json=payload)
print(response.text)