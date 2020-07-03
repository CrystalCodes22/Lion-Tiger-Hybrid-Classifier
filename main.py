import requests
import base64
import json

# Read images from each category
def get_prediction(image_data):
    url = 'https://f9rc0my02e.execute-api.us-east-1.amazonaws.com/Predict/a7c95ca9-45e5-4802-aafa-597f59be7743'
    r = requests.post(url, data=image_data)
    response_raw = getattr(r,'_content').decode("utf-8")
    response = json.loads(response_raw)
    #print(response)
    return response

image_file = 'dog_14.jpeg'

with open(image_file, "rb") as image:
  encoded_image = base64.b64encode(image.read())
  output = get_prediction(encoded_image)
  # Name of your category, for example
  # name could be 'cats' or `dogs`
  print(output, '\n')
  print('predicted label', output['predicted_label'])
  print('score/probability value', output['score'])