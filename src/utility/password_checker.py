from src.model.password import Password


class PasswordChecker:
    @classmethod
    def check_password(cls, password: Password) -> bool:
        if password.length == 0:
            return False

        data_from_class: tuple = (
            password.numbers,
            password.low_case,
            password.up_case,
            password.special_char_1,
            password.special_char_2
        )

        return True in data_from_class
