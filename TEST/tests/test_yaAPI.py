# -*- coding: utf-8 -*-
import pytest
import requests
from ya_API import YandexDisk


def test_dir():
    TOKEN = "*ввести свой токен"
    ya = YandexDisk(token=TOKEN)
    path = 'test_'
    result = ya.dir(path)
    assert result == 201
