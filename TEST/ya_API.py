from pprint import pprint

import requests

TOKEN = "y0_AgAAAAAZp6RgAADLWwAAAADMjkKCEB6IGR2WRL6MQbzh6sI8YVzF99Q"
class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def dir(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        response = requests.put(url, headers=self.get_headers(), params=params)
        return response.status_code


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.dir

