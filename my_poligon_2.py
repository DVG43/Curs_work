from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_file(self, file_link, disk_file_path):
        headers = self.get_headers()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = { "url": file_link, "path": disk_file_path, "overwrite": False}
        r = requests.post(url=upload_url, params=params, headers=headers)
        res = r.json()
        pprint (res)

if __name__ == '__main__':

    token = '********************'
    putloader = YaUploader(token)
    n_foto ='https://sun9-28.userapi.com/impf/c850732/v850732336/16fa43/3b7pxN3vzmI.jpg?size=130x130&quality=96&sign=3bc4940480ccdd72ed3a45c6ad0084c1&c_uniq_tag=_RwR_u87lbDr-wyd0SRMMmOD03HjPwjaPNW3PIcpwhc&type=album'
    path_yandex = '/photo/begemot1'
    putloader.get_upload_file( n_foto, path_yandex)



 #path_yandex = 'https://disk.yandex.ru/client/disk/photo'



#AQAAAABbqfAeAADLW0ZHggdGL0GIpWWHzWBa9gI