from src.model.password import Password


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
        self._special_char_1 = tuple("!#$%&()*+,-./:;=?@[]{|}")
        self._special_char_2 = tuple("<>^~¢£§¬")

    def generate_password(self, password: Password) -> str | None:
        return None
