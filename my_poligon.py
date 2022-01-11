import requests
from pprint import pprint

URL = 'https://api.vk.com/method/users.get'
token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
params = {
    'user_id' : '1000',
    'access_token' : token,
    'v' : '5.131'
}
res = requests.get(URL,params=params)
pprint(res.json())
