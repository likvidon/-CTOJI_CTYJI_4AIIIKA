#### НЕ ПОЛУЧИЛОСЬ РЕАЛИЗОВАТЬ ####
import requests
import json

res = requests.get('https://www.visionhub.ru/api/v2/auth/generate_token/')
token = str(json.loads(res.text)['token'])
data = {
    'model': 'face-blurring',
}
res = requests.post('https://www.visionhub.ru/api/v2/process/img2img/?process_type=img2img',
    headers = {"Authorization": "Bearer " + token, "Content-Type": 'multipart/form-data'},  
    files = {'image': open('./users_images/215340812.jpg', 'rb'), 'model': 'face-blurring'}),

print(res[0].text) 
