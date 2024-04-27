from random import choice

from src.model.password import Password
from src.utility.password_utility import get_not_none_keys


class Generate:
    _numbers: tuple[str, ...]
    _low_case: tuple[str, ...]
    _up_case: tuple[str, ...]
    _special_char_1: tuple[str, ...]
    _special_char_2: tuple[str, ...]

    def __init__(self):
        self._numbers = tuple(str(v) for v in range(10))
        self._low_case = tuple(chr(v) for v in range(97, 123))
        self._up_case = tuple(chr(v) for v in range(65, 91))
        self._special_char_1 = tuple(v for v in "!#$%&()*+,-./:;=?@[]{|}")
        self._special_char_2 = tuple(v for v in "<>^~¢£§¬")

    def generate_password(self, password: Password) -> str | None:
        data_to_select: dict = {
            "numbers": self._numbers,
            "low_case": self._low_case,
            "up_case": self._up_case,
            "special_char_1": self._special_char_1,
            "special_char_2": self._special_char_2,
        }

        valid_keys: tuple = tuple(v for v in get_not_none_keys(password))

        new_password: str = ""

        for _ in range(password.length):
            chosen_key: str = choice(valid_keys)

            chosen_value: str = choice(data_to_select.get(chosen_key))

            new_password += chosen_value

        return new_password
