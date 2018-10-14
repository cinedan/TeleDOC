import requests
import json


def sendData(uid=-1, pillCount=-1, drugName=""):
    post_data = {
        "pill_count" : pillCount, "drugName" : drugName, "uid" : uid
    }
    r = requests.post("http://10.10.3.97:8000/client_update", data=post_data)
    print(json.loads(r.text))


def reqData():
    post_request = {
        ""
    }
    r = requests.post("http://10.10.3.97:8000/schedule", data={'dispenser_uid': 1})
    print(json.loads(r.text))


if __name__ == '__main__':
    sendData(uid=1, pillCount=13, drugName="cocaine")
