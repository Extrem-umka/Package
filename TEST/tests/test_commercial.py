# -*- coding: utf-8 -*-
import pytest
from commercial import commercial

FIXTURE = [
    ('facebook'),
    ('yandex'),
    ('vk'),
    ('google'),
    ('email'),
    ('ok')
]


@pytest.mark.parametrize('k', FIXTURE)
def test_commercial(k):
    result = commercial()
    assert result == k
