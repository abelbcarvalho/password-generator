from src.model.password import Password
from src.service.service_password import ServicePassword


class ControllerPassword:
    _service: ServicePassword

    def __init__(self):
        self._service = ServicePassword()

    def generate_password(self, password: Password) -> str | None:
        return self._service.generate_password(password=password)
