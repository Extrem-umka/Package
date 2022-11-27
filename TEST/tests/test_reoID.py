# -*- coding: utf-8 -*-
import pytest
from reoID import reoID

FIXTURE = [
    ({98, 35, 15, 213, 54, 119}),
    ({98, 35, 213, 213, 54, 119}),
    ({98, 35, 15, 213, 54, 54}),
    ({77}),
    ({})
]


@pytest.mark.parametrize('val', FIXTURE)
def test_reoID(val):
    result = reoID()
    assert result == val

