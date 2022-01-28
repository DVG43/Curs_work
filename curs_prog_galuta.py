
import requests
from pprint import pprint
import json

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
    date_foto = any_foto['date']
    name_of_file = f'{cvont_likes} {date_foto}'
    size_of_file = geting_max_size_foto(any_foto['sizes'])
    any_foto_info = {"file_name": name_of_file, "size":size_of_file}
    return any_foto_info

#pprint(resalult_ror_every_foto) #печать файла с результатами
#pprint(every_links_foto) #печать ссылок фото


class YaUploader: #Класс для записи объекта на лиск яндекса
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
        }

    def geting_directory(self):  # Метод класса для получения папки.
        headers = self.get_headers()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"overwrite": False}
        r = requests.get(url=upload_url, params=params, headers=headers)
        res = r.json()
        pprint(res)


    def making_directory(self, name_directory):  # Метод класса для формирования папки.
        headers = self.get_headers()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"url": name_directory,  "overwrite": False}
        r = requests.put(url=upload_url, params=params, headers=headers)
        res = r.json()
        pprint(res)

    def get_upload_file(self, file_link, disk_file_path): #Метод класса для записи файла на яндес.
        headers = self.get_headers()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = { "url": file_link, "path": disk_file_path, "overwrite": False}
        r = requests.post(url=upload_url, params=params, headers=headers)
        res = r.json()
        pprint (res)



#
if __name__ == '__main__':

    # блок работы по получению фотографий из в контакте
    token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    URL = 'https://api.vk.com/method/account.getProfileInfo'
    params = {
        'account': 'begemot_korovin',
        'access_token': token,
        'v': '5.131'
    }
    res_1 = requests.get(URL, params=params)
    pprint(res_1.json())  # Получаем данные пользователя
    res_2 = res_1.json()
    personal_id = str(res_2['response']['id'])  # получили ID

    # response = request["response"]
    # if response["type"] != "user":
    #     raise MyException("Невалидный идентифиикатор пользователя")

    URL = 'https://api.vk.com/method/photos.get'  # Получение фото со стены
    params = {
        'owner_id': f'{personal_id}',
        'album_id': 'profile',
        'extended': 1,
        'photo_sizes': 0,
        'access_token': token,
        'v': '5.131'
    }
    res = requests.get(URL, params=params)
    resalt = res.json()
    foto_list = resalt['response']['items']  # Получен список фсех фото с параметрами фото

    # формирование переменных по полученным из вк данных
    resalult_ror_every_foto = []
    every_links_foto = []
    for foto_in_list in foto_list:
        resalult_ror_every_foto.append(making_info_for_foto(foto_in_list))  # Список для записи результата в файл и
        # ормирования имени файла.
        every_links_foto.append(
            geting_links_foto(foto_in_list['sizes']))  # Список ссылок на файлы которые уйдут в яндекс.


    # блок работы с яндексом
    token_yandex = 'AQAAAABbqfAeAADLW0ZHggdGL0GIpWWHzWBa9gI'
    putloader = YaUploader(token_yandex) #Запись элемента класса на диск яндекса
    index = 0
    name_foto = ''

    putloader.geting_directory()
    putloader.making_directory("/photo/")

    for one_foto in every_links_foto: #Цикл записи фото на яндекс диск
            n_foto = one_foto
            name_foto = resalult_ror_every_foto[index]['file_name']
            path_yandex = f'/photo/{name_foto}'
            putloader.get_upload_file( n_foto, path_yandex)
            index += 1

    with open('rezalt_file.json', 'w') as f: #Запись в корнефой каталог фвайла результа.
        json.dump(resalult_ror_every_foto,f,indent = 2)
