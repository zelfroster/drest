import requests

product_id = input("Please enter a product id to delete: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid id')

endpoint = f"http://localhost:5000/api/products/{product_id}/delete/"

response = requests.delete(endpoint)

# print(response.json())
# print(response.text)
print(response.status_code)
if response.status_code == 204:
    print("DELETED")
