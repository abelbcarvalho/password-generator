from typing import Generator, Any

from src.model.password import Password


def get_not_none_keys(password: Password) -> Generator[str, Any, None]:
    not_none_keys: dict = {
        "numbers": password.numbers,
        "low_case": password.low_case,
        "up_case": password.up_case,
        "special_char_1": password.special_char_1,
        "special_char_2": password.special_char_2,
    }

    return (v for v in not_none_keys.keys() if not_none_keys[v] is True)
