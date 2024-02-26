import requests

endpoint = "http://localhost:5000/api/products/8/"
response = requests.get(endpoint)

print(response.json())
# print(response.text)
# print(response.status_code)
