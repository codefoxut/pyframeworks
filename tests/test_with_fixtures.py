import pytest


def test_with_testclient(client):

    response = client.get('/polls/')
    assert response.status_code == 200


def test_changing_settings(settings):
    settings.DATE_FORMAT = 'Y-m-d'