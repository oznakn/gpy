import requests

headers = {"charset": "utf-8", "Content-Type": "application/json"}
server_url = 'https://gpy-link-redirect.herokuapp.com/save'

path = input('Path: ')
url = input('Url: ')

r = requests.post(server_url, json={ "path": path, "url": url }, headers=headers)
print(r.text)
