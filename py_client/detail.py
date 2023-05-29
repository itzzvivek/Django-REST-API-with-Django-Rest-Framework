import requests

endpoint =  "http://localhost:8000/api/products/1/"

get_response = requests.get(endpoint, json={"content":"Hello World", "content":"Hello World","price":"abc134"}) 

print(get_response.json())





















