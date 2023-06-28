import requests
import os
from dotenv import load_dotenv, find_dotenv


class YaUploader:
    def __init__(self, tokens: str):
        self.url = None
        self.token = tokens

    def get_headers(self):
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        return headers

    def get_upload(self, name_folder):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": name_folder, "url": url}
        response = requests.put(url, headers=headers, params=params)
        return response.status_code


load_dotenv(find_dotenv())
akk_ya = YaUploader(os.getenv('YA_TOKEN'))
