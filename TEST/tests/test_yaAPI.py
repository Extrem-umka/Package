# -*- coding: utf-8 -*-
import pytest
import requests
from ya_API import YandexDisk


def test_dir():
    TOKEN = "y0_AgAAAAAZp6RgAADLWwAAAADMjkKCEB6IGR2WRL6MQbzh6sI8YVzF99Q"
    ya = YandexDisk(token=TOKEN)
    path = 'test_'
    result = ya.dir(path)
    assert result == 201