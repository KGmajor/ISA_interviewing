import pytest


from app import create_app


@pytest.fixture(scope='function')
def app():
    return create_app()
