import pytest
import requests
import config

def create_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(url, params={'path': path}, headers={'Authorization': config.TOKEN})
    return response.status_code

@pytest.fixture
def preparation():
    print('\nStart test')
    yield
    print('\nEnd test')

@pytest.mark.parametrize(
    'path', ['test', 'test/image']
)
def test_api_yandex_one(preparation, path):
    response = create_folder(path)
    assert response == 201, f'Не удалось создать папку по указанному пути: {path}. Код ошибки: {response}'

@pytest.mark.parametrize(
    'path', ['test', 'test/image']
)
@pytest.mark.xfail
def test_api_yandex_two(preparation, path):
    response = create_folder(path)
    assert response == 201, f'Не удалось создать папку по указанному пути: {path}. Код ошибки: {response}'
