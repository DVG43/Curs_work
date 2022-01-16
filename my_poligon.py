import requests
from pprint import pprint

# URL = 'https://api.vk.com/method/users.get'
token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
URL = 'https://api.vk.com/method/account.getProfileInfo'
params = {
    'account':'begemot_korovin',
    'access_token' : token,
    'v' : '5.131'
}
res = requests.get(URL,params=params)
pprint(res.json())

#token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
URL = 'https://api.vk.com/method/photos.get'
params = {
    'owner_id' : '552934290',
    'album_id' : 'profile',
    'extended' : 1,
    'photo_sizes' : 0,
    'access_token' : token,
    'v' : '5.131'
}
res = requests.get(URL,params=params)
resalt = res.json()
foto_list = resalt ['response'] ['items']
pprint(foto_list)

#Получение ссылки на максимальный файл.
def geting_links_foto (list_of_size):
    links_of_foto = ''
    max_size_foto = 0
    for any_foto in list_of_size:
        if any_foto['height'] > max_size_foto:
            max_size_foto = any_foto['height']
            links_of_foto = any_foto['url']
    return links_of_foto

#Получение размеров файла
def geting_max_size_foto (list_of_size):
    size_of_foto = ''
    max_size_foto = 0
    for any_foto in list_of_size:
        if any_foto['height'] > max_size_foto:
            max_size_foto = any_foto['height']
            max_size_foto_2 = any_foto['width']
            size_of_foto = f'h={max_size_foto} X  w={max_size_foto_2}'
    return size_of_foto

#Получение название файла.
def making_info_for_foto (any_foto):
    cvont_likes = any_foto['likes']['count']
    date_foto = any_foto['likes']
    name_of_file = f'{cvont_likes} {date_foto}'
    size_of_file = geting_max_size_foto(any_foto['sizes'])
    any_foto_info = {"file_name": name_of_file, "size":size_of_file}
    return any_foto_info

#Общий алгоритм
resalult_ror_every_foto = []
every_links_foto = []
for foto_in_list in foto_list:
    resalult_ror_every_foto.append(making_info_for_foto(foto_in_list))
    every_links_foto.append(geting_links_foto(foto_in_list['sizes']))

pprint(resalult_ror_every_foto)
pprint(every_links_foto)


#Подпрограмма  выделяющая  нужную ссылку на фото




# account.getProfileInfo
# begemot_korovin
#.json()
