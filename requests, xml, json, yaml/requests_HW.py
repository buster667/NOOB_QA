import requests

req = requests.get('https://fakerestapi.azurewebsites.net/')
print(req)

"""get authors info"""
authors_list = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
print(authors_list)
author_id = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/12')
print(author_id)

"""post"""
url = 'https://fakerestapi.azurewebsites.net/api/v1/Books'
param_dict = {
  "id": 10,
  "title": "",
  "description": "",
  "pageCount": 12,
  "excerpt": "",
  "publishDate": "2022-01-04T09:43:44.482Z"
}
response = requests.post(url, json=param_dict)
print(response)

url2 = 'https://fakerestapi.azurewebsites.net/api/v1/Users/'

user_param = {
  "id": 123,
  "userName": "Egor",
  "password": "qwerty123"
}
second_response = requests.post(url, json=user_param)
print(second_response)

"""PUT"""
new_id_param = {
  "id": 123
}
new_info = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=new_id_param)
print(new_info)

"""DELETE"""
delete_user = requests.delete('https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(delete_user)
