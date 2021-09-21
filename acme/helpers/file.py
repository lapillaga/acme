from acme.common.exceptions import FileNotFoundException
from pathlib import Path


RESOURCES_PATH = '../resources'


def read_lines_from_file(file_name):
    try:
        path = get_file_path(file_name)
        with open(path, mode='r') as text:
            lines = text.read().splitlines()
        return lines
    except FileNotFoundError:
        raise FileNotFoundException(file_name)


def get_file_path(file_name):
    base_path = Path(__file__).parent
    file_path = (base_path / RESOURCES_PATH / file_name).resolve()
    return file_path
