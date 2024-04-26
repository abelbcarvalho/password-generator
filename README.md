# Password Generator
Generate strong passwords.

## SUMMARY
1. [Description](#description)
2. [Valid Characters](#valid-characters)
2. [Dependencies](#dependencies)
3. [Model Structure](#model-structure)
4. [How It Works?](#how-it-works)
5. [System Steps](#system-steps)
6. [The End](#the-end)

### Description
*This software has the intent of generate strong passwords to you set into the register of web services. You just need to set your options, then our system will take your information to generate random passwords and set it to the clipboard area.*

### Valid Characters
The generated password can contain:

1. Numbers `0 ... 9`;
2. Lowcase `a ... z`;
3. Upcase `A ... Z`;
4. Special Characters 1 `$#,.]:[(;)}|!{?+=-*/%&@`;
5. Special Characters 2 `¢¬§£><\~^`;

### Dependencies
1. Python3;
2. Pip;
3. Clipboard;
4. Tkinter;

> **NOTE:** The project dependencies list can be found on the file [requirements.txt](#)

To install the requirement.txt file, just type or paste it on a Terminal window:

```commandline
pip install -r requirement.txt
```

### Model Structure
Here you can see the class structure to send data to back-end.

* **Password**

| attribute      | type | default |
|:---------------|:-----|:--------|
| numbers        | bool | None    |
| lowcase        | bool | None    |
| upcase         | bool | None    |
| special_char_1 | bool | None    |
| special_char_2 | bool | None    |
| length         | int  | 0       |

### How It Works?
Description about the steps this software works. It's divided between *User* and *System* requirements.

> **User Requirements:**

1. You choose the characters you want to use;
2. You select the length of your required password;
3. You send these informations to back-end;

> **System Requirements:**

4. System receives the `model` sent by User;
5. So this model is checked, (at least 1 attribute must be `True` value);
5.1. If valid not valid, launch a new exception;
6. count the length and required values range;
7. Use `random.choice` method to get a value and join to the password string;
8. Set the **generated password** to clipboard and returns to the *highest level;*
9. Set the **generated password** to be seen by user;

### System Steps
A resume of [*how it works?*](#how-it-works)

1. User choose paramenters;
2. Check paramenters;
3. Generate password;
4. Transfer to *clipboard* area;
5. Return the generated password;
6. Let it be seen by user;

### The End
It's a simple project task to make an userful software.

-- *Abel Carvalho*

*That's all folks!!!*
