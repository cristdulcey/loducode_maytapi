import json

import requests

id_phone = "3317"
product_id = "f99d87b0-a9d7-44e8-bd1a-93b9fffc09f1"
base_url = f"https://api.maytapi.com/api/{product_id}"
token = '0af36ce9-c28e-4e02-a2f9-fee64ffe6c99'
headers = {
    'content-type': 'application/json',
    'x-maytapi-key': token
}


def send_text(phone: str, text: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        'type': 'text',
        'message': text
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def send_multimedia(phone: str, text: str, url_media: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        'type': 'media',
        'message': url_media,
    }
    if text:
        payload["text"] = text
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def send_contact(phone: str, contact: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        'type': 'contact',
        'message': contact,
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def send_forward(phone: str, chatId: str, msgId: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        'type': 'forward',
        'message': f"false_{chatId}_{msgId}",
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def send_reply(phone: str, message: str, chatId: str, msgId: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        'type': 'text',
        'message': message,
        'reply_to': f"false_{chatId}_{msgId}",
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def send_location(phone: str, message: str, latitude: str, longitude: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        "type": "location",
        "text": message,
        "latitude": latitude,
        "longitude": longitude
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def send_link(phone: str, message: str, url_link: str):
    url = f"{base_url}/{id_phone}/sendMessage"
    payload = {
        'to_number': phone,
        "type": "link",
        "text": message,
        "message": url_link
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        success = response.get("success")
        data = response.get("data")
        return success, data
    else:
        return False, {}


def set_webhook(url_server: str):
    url = f"{base_url}/setWebhook"
    payload = {
        'webhook': url_server,
    }
    req = requests.post(url, data=json.dumps(payload), headers=headers)
    if req.status_code == 200:
        response = req.json()
        pid = response.get("pid")
        webhook = response.get("webhook")
        ack_delivery = response.get("ack_delivery")
        phone_limit = response.get("phone_limit")
        response_dict = {
            "pid":pid,
            "webhook":webhook,
            "ack_delivery":ack_delivery,
            "phone_limit":phone_limit,
        }
        return True, response_dict
    else:
        return False, {}


send_text("573166187553@c.us","hello world 😄")
# send_multimedia("573166187553@c.us","hello world 😄","http://oyepepe.com/static/dashboard/assets/images/logo.png")
# send_multimedia("573166187553@c.us","","http://oyepepe.com/static/dashboard/assets/images/logo.png")
# send_contact("573166187553@c.us",'573166187553@c.us')
# send_location("573166187553@c.us","Hello","12.654","-72.776")
# send_location("573166187553@c.us","","12.654","-72.776")
# send_link("573166187553@c.us","Text","https://google.com")
# send_link("573166187553@c.us","","https://google.com")
# set_webhook("https://f2d55e5eceae.ngrok.io/chatbot/recibir-mensage/")

# NOT WORKING
# send_forward("573166187553","573162557014@c.us","87f667a0-be38-11ea-9422-99a655694b14")
# send_reply("573166187553@c.us","Hello","573166187553@c.us","ad2d6c70-be39-11ea-894e-d7d465b17ba0")
