import pytest
from core.app import app

from flask import Flask


@pytest.fixture()
def flask_app():
    yield app


@pytest.fixture()
def client(flask_app: Flask):
    return flask_app.test_client()


@pytest.fixture()
def runner(flask_app: Flask):
    return flask_app.test_cli_runner()
