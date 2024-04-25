import requests

chat_id = "-1001982477273"
urlp = "https://t.me/X4_fT"
url = f"https://api.telegram.org/botتوكن بوتك/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
