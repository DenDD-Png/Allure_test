from pathlib import Path
import os
import allure
from selene import browser


@allure.step("Выбираем аватарку")
def get_resource_path(file_name):
   # Поднимаемся на 2 уровня выше от текущего файла (если tests в корне проекта)
    base_dir = Path(__file__).parent.parent
    resources_dir = base_dir / 'tests' / 'resources'
    file_path = resources_dir / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_name} не найден в {resources_dir}")

    return str(file_path.absolute())


def upload_picture(file_name):

    file_path = get_resource_path(file_name)
    browser.element('#uploadPicture').send_keys(file_path)