from os import path
from typing import Any, Dict
import yaml

# noinspection PyBroadException
try:
    project_path = path.dirname(path.dirname(path.realpath(__file__)))
    config_file_name = path.join(project_path, 'config.yaml')
    with open(config_file_name, 'r') as fp:
        config: Dict[str, Any] = yaml.safe_load(fp)
except Exception as ex:
    print(f'Exception occurred while loading config: {ex}')
    config: Dict[str, Any] = {}

import pr.db
import pr.web
import pr.utils

__db_controller: pr.db.DBController = None


def get_db_controller() -> 'pr.db.DBController':
    global __db_controller
    if __db_controller is None:
        __db_controller = pr.db.DBController()
    return __db_controller
