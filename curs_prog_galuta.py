
# with open('token.txt','r') as file_object:
#      token = file_object.read().strip()

# impotr time
import requests
from pprint import pprint

# URL = 'https://api.vk.com/method/users.get'

# Пишем класс для инициализации.
class Vk_user:
     URL = 'https://api.vk.com/method/'
     def __init__(self, token, version):
          self.params = {
               'access_token' : token,
               'ver' : version
          }

# Пишем методы для класса.
     # Параметры sort:
     # 0 - по умолчанию
     # 1 - по скорости роста
     # 2 - по отошению дневной посещаемости
     # 3 - по отношениею количества лайков к количеству пользователей
     # 4 - по отношению количества комментариев к количеству пользоват
     # 5 - по отношениею количества записей в обсуждениях к количеству пользователей

     def search_groups (self, q, sorting=0):
          group_search_url = self.URL + 'group.search'
          group_search_params = {
               'q':  q,
               'sort':  sorting,
               'count' : 300
          }
          req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
          return req ['response']['items']

if __name__ == '__main__':
     token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
     vk_i_user = Vk_user(token, '5.131')
     pprint (vk_i_user.search_groups('python'))
