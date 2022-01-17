
# with open('token.txt','r') as file_object:
#      token = file_object.read().strip()

#impotr time
import requests
from pprint import pprint

# URL = 'https://api.vk.com/method/users.get'

# Пишем класс для инициализации.

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
                 'access_token': token,
                 'v': version
        }
# Пишем методы для класса.

    def search_groups(self, q, sorting=0):
        group_search_url = self.url + 'groups.search'
        group_search_params = {
              'q': q,
              'sort': sorting,
              'count': 300
          }
        req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
        return req['response']['items']

if __name__ == '__main__':
     token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
     vk_i_user = VkUser(token, '5.131')
     pprint (vk_i_user.search_groups('Михаил Булгаков'))
