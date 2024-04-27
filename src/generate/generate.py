from typing import Generator, Any
from random import choice

from src.model.password import Password
from src.utility.password_utility import get_not_none_keys


class Generate:
    _numbers: Generator[str, Any, None]
    _low_case: Generator[str, Any, None]
    _up_case: Generator[str, Any, None]
    _special_char_1: Generator[str, Any, None]
    _special_char_2: Generator[str, Any, None]

    def __init__(self):
        self._numbers = (str(v) for v in range(10))
        self._low_case = (chr(v) for v in range(97, 123))
        self._up_case = (chr(v) for v in range(65, 91))
        self._special_char_1 = (v for v in "!#$%&()*+,-./:;=?@[]{|}")
        self._special_char_2 = (v for v in "<>^~¢£§¬")

    def generate_password(self, password: Password) -> str | None:
        data_to_select: dict = {
            "numbers": tuple(v for v in self._numbers),
            "low_case": tuple(v for v in self._low_case),
            "up_case": tuple(v for v in self._up_case),
            "special_char_1": tuple(v for v in self._special_char_1),
            "special_char_2": tuple(v for v in self._special_char_2),
        }

        valid_keys: tuple = tuple(v for v in get_not_none_keys(password))

        new_password: str = ""

        for _ in range(password.length):
            chosen_key: str = choice(valid_keys)

            chosen_value: str = choice(data_to_select.get(chosen_key))

            new_password += chosen_value

        return new_password
