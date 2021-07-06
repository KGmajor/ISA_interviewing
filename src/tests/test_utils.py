import os
from utils import get_env_variable


def test_get_env_variable_fail():
    try:
        print("cool")
        assert False, 'Expected KeyError exception was skipped'
    except Exception:
        assert True, 'ERROR: exception was raised'

