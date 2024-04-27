from typing import Generator, Any

from src.model.password import Password


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

    def _get_not_none_keys(self, password: Password) -> Generator[str, Any, None]:
        not_none_keys = {
            "numbers": password.numbers,
            "low_case": password.low_case,
            "up_case": password.up_case,
            "special_char_1": password.special_char_1,
            "special_char_2": password.special_char_2,
        }

        return (v for v in not_none_keys.keys() if not_none_keys[v] is True)

    def generate_password(self, password: Password) -> str | None:
        return None
