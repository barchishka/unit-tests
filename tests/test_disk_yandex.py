from srs.disk_yandex_folder import *
from unittest import TestCase


class TestYandex(TestCase):
    def test_get_upload(self):
        self.assertEqual(akk_ya.get_upload('test'), 201, "folder created")

    def test_get_upload_fail(self):
        self.assertEqual(akk_ya.get_upload('test'), 201, "folder not created")
