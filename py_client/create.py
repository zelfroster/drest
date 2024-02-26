import requests

endpoint = "http://localhost:5000/api/products/"

data = {
    "title": "This field is done",
    "price": 43.89
}

response = requests.post(endpoint, json=data)

print(response.json())
# print(response.text)
# print(response.status_code)
