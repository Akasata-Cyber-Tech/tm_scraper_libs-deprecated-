import requests
import json

url = "https://mocki.io/v1/5859d617-a291-447f-91c8-0e514b4bc87a"
response = requests.get(url)
data = response.json()

# print(response)
print(data)