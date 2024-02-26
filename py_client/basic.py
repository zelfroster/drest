import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:5000/api/?key=value"

response = requests.post(
    endpoint, params={'abc': 123}, json={'title': "Test title", 'content': 'testing'})

# print(response.json())
print(response.text)
# print(response.status_code)
