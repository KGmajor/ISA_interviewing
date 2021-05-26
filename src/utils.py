import os
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def get_env_variable(name) -> str:
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)
