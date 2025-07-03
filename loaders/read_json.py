import json
from typing import Any, Optional


def read_json(filepath: str) -> Optional[Any]:

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)
