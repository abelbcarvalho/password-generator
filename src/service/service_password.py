from src.model.password import Password
from src.generate.generate import Generate
from src.exceptions.exceptions import PasswordCheckerException
from src.utility.password_checker import PasswordChecker


class ServicePassword:
    _generate: Generate

    def __init__(self):
        self._generate = Generate()

    def generate_password(self, password: Password) -> str | None:
        if not PasswordChecker.check_password(password=password):
            raise PasswordCheckerException("error: generate length or generate params whole false")

        return self._generate.generate_password(password=password)
