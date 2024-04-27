from tkinter import (
    Tk, Frame, Entry, Label,
    Checkbutton, Scale, Button,
    HORIZONTAL, LEFT, IntVar
)

from tkinter.messagebox import (
    showinfo,
    showerror,
)

from clipboard import copy as set_to_transfer_area

from src.exceptions.exceptions import PasswordCheckerException
from src.model.password import Password
from src.controller.controller_password import ControllerPassword


def _copy_success() -> None:
    showinfo(
        title='Success',
        message='Your password has been copied to clipboard.'
    )


class PasswordGenerator:
    _password: Password
    _controller_password: ControllerPassword

    def __init__(self, main: Tk):
        font_title = ("Arial", 20, "bold")
        font_entry = ("Verdana", 12)
        font_regular = ("Arial", 14)
        font_regular_bold = ("Arial", 14, "bold")

        length_entry = 66
        length_checkbox = 360

        # colors
        white = "#ffffff"
        red = "#ff0000"
        dark_blue = "#000044"
        black = "#000000"
        gold = "#ffd700"

        # window create
        main.title("Password Generator")
        main.geometry("720x360")
        main.resizable(False, False)
        main["bg"] = white

        # new password and controller instances
        self._password = Password()
        self._controller_password = ControllerPassword()

        # title frame
        self.title_frame = Frame(main)
        self.title_frame["bg"] = white
        self.title_frame.pack()

        self.title_label = Label(self.title_frame)
        self.title_label["text"] = "Password Generator"
        self.title_label["font"] = font_title
        self.title_label["bg"] = white
        self.title_label["fg"] = black
        self.title_label.pack()

        # length size
        self.length_frame = Frame(main)
        self.length_frame["bg"] = white
        self.length_frame.pack()

        self.label_length = Label(self.length_frame)
        self.label_length["text"] = "Length Password (max. 128 characters) *"
        self.label_length["font"] = font_regular
        self.label_length["bg"] = white
        self.label_length.pack()

        self.scale_length = Scale(self.length_frame, from_=0, to=128, orient=HORIZONTAL)
        self.scale_length["length"] = 360
        self.scale_length["bg"] = white
        self.scale_length["highlightbackground"] = white
        self.scale_length["troughcolor"] = gold
        self.scale_length.pack()

        # variables check buttons
        self.value_check_numbers = IntVar()
        self.value_check_low_case = IntVar()
        self.value_check_up_case = IntVar()
        self.value_check_special_one = IntVar()
        self.value_check_special_two = IntVar()

        # choose characters # check buttons
        self.character_frame = Frame(main)
        self.character_frame["bg"] = white
        self.character_frame.pack()

        self.check_numbers = Checkbutton(self.character_frame)
        self.check_numbers["text"] = "Numbers: 0 ... 9                                "
        self.check_numbers["font"] = font_regular
        self.check_numbers["width"] = length_checkbox
        self.check_numbers["variable"] = self.value_check_numbers
        self.check_numbers["bg"] = white
        self.check_numbers["highlightbackground"] = white
        self.check_numbers["activebackground"] = gold
        self.check_numbers.pack()

        self.check_low_case = Checkbutton(self.character_frame)
        self.check_low_case["text"] = "Lowercase: a ... z                              "
        self.check_low_case["font"] = font_regular
        self.check_low_case["width"] = length_checkbox
        self.check_low_case["variable"] = self.value_check_low_case
        self.check_low_case["bg"] = white
        self.check_low_case["highlightbackground"] = white
        self.check_low_case["activebackground"] = gold
        self.check_low_case.pack()

        self.check_up_case = Checkbutton(self.character_frame)
        self.check_up_case["text"] = "Uppercase: A ... Z                             "
        self.check_up_case["font"] = font_regular
        self.check_up_case["width"] = length_checkbox
        self.check_up_case["variable"] = self.value_check_up_case
        self.check_up_case["bg"] = white
        self.check_up_case["highlightbackground"] = white
        self.check_up_case["activebackground"] = gold
        self.check_up_case.pack()

        self.check_special_one = Checkbutton(self.character_frame)
        self.check_special_one["text"] = "Special One: !#$%&()*+,-./:;=?@[]{|}"
        self.check_special_one["font"] = font_regular
        self.check_special_one["width"] = length_checkbox
        self.check_special_one["variable"] = self.value_check_special_one
        self.check_special_one["bg"] = white
        self.check_special_one["highlightbackground"] = white
        self.check_special_one["activebackground"] = gold
        self.check_special_one.pack()

        self.check_special_two = Checkbutton(self.character_frame)
        self.check_special_two["text"] = "Special Two: <>^~¢£§¬                    "
        self.check_special_two["font"] = font_regular
        self.check_special_two["width"] = length_checkbox
        self.check_special_two["variable"] = self.value_check_special_two
        self.check_special_two["bg"] = white
        self.check_special_two["highlightbackground"] = white
        self.check_special_two["activebackground"] = gold
        self.check_special_two.pack()

        # entry field with the generated password
        self.passwd_frame = Frame(main)
        self.passwd_frame["bg"] = white
        self.passwd_frame.pack()

        self.entry_passwd = Entry(self.passwd_frame)
        self.entry_passwd["font"] = font_entry
        self.entry_passwd["width"] = length_entry
        self.entry_passwd["bg"] = white
        self.entry_passwd["highlightbackground"] = black
        self.entry_passwd["highlightcolor"] = black
        self.entry_passwd["selectbackground"] = gold
        self.entry_passwd["selectforeground"] = black
        self.entry_passwd["border"] = 0
        self.entry_passwd.pack(pady=20)

        # buttons
        self.button_frame = Frame(main)
        self.button_frame["bg"] = white
        self.button_frame.pack()

        self.button_generate = Button(self.button_frame)
        self.button_generate["text"] = "Generate"
        self.button_generate["font"] = font_regular_bold
        self.button_generate["width"] = 20
        self.button_generate["bg"] = dark_blue
        self.button_generate["fg"] = white
        self.button_generate["border"] = 0
        self.button_generate["activebackground"] = gold
        self.button_generate["activeforeground"] = black
        self.button_generate.bind("<Button-1>", self._generate_password)
        self.button_generate.pack(side=LEFT, padx=5)

        self.button_copy = Button(self.button_frame)
        self.button_copy["text"] = "Copy"
        self.button_copy["font"] = font_regular_bold
        self.button_copy["width"] = 20
        self.button_copy["bg"] = red
        self.button_copy["fg"] = white
        self.button_copy["border"] = 0
        self.button_copy["activebackground"] = gold
        self.button_copy["activeforeground"] = black
        self.button_copy.bind("<Button-1>", self._copy_to_transfer_area)
        self.button_copy.pack(side=LEFT, padx=5)

        # visible
        main.mainloop()

    def _generate_password(self, event) -> None:
        boolean: tuple = (False, True)

        self._password.length = self.scale_length.get()

        self._password.numbers = boolean[self.value_check_numbers.get()]
        self._password.low_case = boolean[self.value_check_low_case.get()]
        self._password.up_case = boolean[self.value_check_up_case.get()]
        self._password.special_char_1 = boolean[self.value_check_special_one.get()]
        self._password.special_char_2 = boolean[self.value_check_special_two.get()]

        try:
            new_password = self._controller_password.generate_password(password=self._password)

            self.entry_passwd.delete(0, "end")

            self.entry_passwd.insert(0, new_password)
        except PasswordCheckerException as ex:
            message = ex.args[0]

            showerror(title="Error to Generate Password", message=message.capitalize())

    def _copy_to_transfer_area(self, event) -> None:
        content_password = self.entry_passwd.get()

        set_to_transfer_area(content_password)

        _copy_success()
