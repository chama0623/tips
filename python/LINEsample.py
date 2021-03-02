# send start and finish time to LINE
import requests
import datetime

dt_start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# write process


dt_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

s = "\nstart time : "+dt_start+"\nfinish time : "+dt_end

token = "xxx"
url = "https://notify-api.line.me/api/notify"
headers = {"Authorization": "Bearer " + token}
payload = {"message": s}
requests.post(url, headers=headers, data=payload)