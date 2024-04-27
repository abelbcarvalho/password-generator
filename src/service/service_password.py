from src.model.password import Password
from src.exceptions.exceptions import PasswordCheckerException
from src.utility.password_checker import PasswordChecker


class ServicePassword:
    def generate_password(self, password: Password) -> str | None:
        if not PasswordChecker.check_password(password=password):
            raise PasswordCheckerException("error: generate length or generate params whole false")

        return None
