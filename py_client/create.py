import requests


headers = {'Authorization' : 'Bearer 6cbc90f03a79b9bd0f4e94525c0a24dd6c9bfa8c'}
endpoint = "http://localhost:8000/api/products/"

data = {
    'title' : 'this field is done',
    'price' : 32.99
}

get_response = requests.post(endpoint, json=data,headers=headers)
print(get_response.json())