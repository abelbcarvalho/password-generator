from tkinter import Tk

from src.view.password_generator import PasswordGenerator


def main() -> None:
    root = Tk()

    PasswordGenerator(root)


if __name__ == '__main__':
    main()
