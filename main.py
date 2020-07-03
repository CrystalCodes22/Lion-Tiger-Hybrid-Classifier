import requests
import base64
import json

def get_prediction(image_data):
    url = 'https://f9rc0my02e.execute-api.us-east-1.amazonaws.com/Predict/601839cc-9589-435c-8a14-c9e4e5ac94d7'
    r = requests.post(url, data=image_data)
    response = getattr(r,'_content').decode("utf-8")
    print(response)
    return response
with open("<image_location>", "rb") as image:
    payload = base64.b64encode(image.read()
response = get_prediction(payload)