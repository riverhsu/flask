import requests

# 傳送 payload ,請求回覆
def senddata():
	payload = {"name":"river", "age":54}
	url = "http://192.168.209.128:5000/getpayload"
	r = requests.request("POST", url, json=payload, headers={"content-type":"application/json"})
	print(r.text)

senddata()