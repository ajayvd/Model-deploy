import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'X':2, 'X_SQUARE':9})

print(r.json())