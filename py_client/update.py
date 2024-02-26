import requests

endpoint = "http://localhost:5000/api/products/8/update/"

data = {
    "title": "test update",
    "price": 123.44
}

response = requests.put(endpoint, json=data)

print(response.json())
# print(response.text)
# print(response.status_code)
