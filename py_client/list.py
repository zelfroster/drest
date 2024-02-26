import requests

endpoint = "http://localhost:5000/api/products/"

data = {
    "title": "This field is done",
    "price": 43.89
}

response = requests.get(endpoint)

print(response.json())
