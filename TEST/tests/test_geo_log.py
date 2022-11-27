# -*- coding: utf-8 -*-
import pytest
from geo_log import geo_log

FIXTURE = [
    ([{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]),
    ([{'visit1': ['Москва', 'Россия']}, {'visit3': ['Лиссабон', 'Португалия']}, {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]),
    ([{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit5': ['Париж', 'Франция']},
      {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])
]


@pytest.mark.parametrize('result_list', FIXTURE)
def test_geo_log(result_list):
    result = geo_log()
    assert result == result_list

