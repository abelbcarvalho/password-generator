# Password Generator
Generate strong passwords.

## SUMMARY
1. [Description](#description)
2. [Valid Characters](#valid-characters)
2. [Dependencies](#dependencies)
3. [How To Run?](#how-to-run)
4. [Model Structure](#model-structure)
5. [How It Works?](#how-it-works)
6. [System Steps](#system-steps)
7. [Possible Questions](#possible-questions)
8. [Appearance](#appearance)
9. [The End](#the-end)

### Description
*This software has the intent of generate strong passwords to you set into the register of web services. You just need to set your options, then our system will take your information to generate random passwords and set it to the clipboard area.*

*It is a Desktop application, so you can find it appearance [here](#appearance).*

### Valid Characters
The generated password can contain:

1. Numbers `0 ... 9`;
2. Low Case `a ... z`;
3. Up Case `A ... Z`;
4. Special Characters 1 `!#$%&()*+,-./:;=?@[]{|}`;
5. Special Characters 2 `<>^~¢£§¬`;

### Dependencies
1. Python3;
2. Pip;
3. Clipboard;
4. Tkinter;

> **NOTE:** The project dependencies list can be found on the file [requirements.txt](requirements.txt)

To install the requirement.txt file, just type or paste it on a Terminal window:

**Have a problem?** Please visite the section of [questions](#possible-questions) here. Possible cases are about the
*tkinter* and *clipboard* libraries, mainly referring to *linux operating system*.

```commandline
pip install -r requirement.txt
```

### How To Run?
Please review the last Chapter *Dependencies* and install them all. If it ran successfully, you are ready to run.

To make it, just run the file: [`app.py`](/app.py). It is configured.

On the root directory [here](/) of that project, just type:

For Windows:

```commandline
py app.py
```

For MacOS:

```commandline
python app.py
```

For Linux Distros:

```commandline
python3 app.py
```

**If you find a problem**, review [dependencies](#dependencies) chapter.

### Model Structure
Here you can see the class structure to send data to back-end.

* **Password**

| attribute      | type | default |
|:---------------|:-----|:--------|
| numbers        | bool | None    |
| low_case       | bool | None    |
| up_case        | bool | None    |
| special_char_1 | bool | None    |
| special_char_2 | bool | None    |
| length         | int  | 0       |

### How It Works?
Description about the steps this software works. It's divided between *User* and *System* requirements.

> **User Requirements:**

1. You choose the characters you want to use;
2. You select the length of your required password;
3. You send these information to back-end;

> **System Requirements:**

1. System receives the `model` sent by User;
2. So this model is checked, (at least 1 attribute must be `True` value); 
   1. If valid not valid, launch a new exception;
3. count the length and required values range;
4. Use `random.choice` method to get a value and join to the password string;
5. Set the **generated password** to clipboard and returns to the *highest level;*
6. Set the **generated password** to be seen by user;

### System Steps
A resume of [*how it works?*](#how-it-works)

1. User choose parameters;
2. Check parameters;
3. Generate password;
4. Transfer to *clipboard* area;
5. Return the generated password;
6. Let it be seen by user;

### Possible Questions

<details>
   <summary>
      Clipboard Library Problem?
   </summary>
   <p>
      You may get an error message that says: “Pyperclip could not find a copy/paste mechanism for your system. Please see <a target="_blank" href="https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error">clipboard library docs</a> for how to fix this.”
   </p>
   <p>
      In order to work equally well on Windows, Mac, and Linux, Pyperclip uses various mechanisms to do this. Currently, this error should only appear on Linux (not Windows or Mac). You can fix this by installing one of the copy/paste mechanisms:
   </p>
   <p>
      <ul>
         <li><code>sudo apt install xsel</code> to install the xsel utility.</li>
         <li><code>sudo apt install xclip</code> to install the xclip utility.</li>
         <li><code>pip install gtk</code> to install the gtk Python module.</li>
         <li><code>pip install PyQt4</code> to install the PyQt4 Python module.</li>
      </ul>
   <p>
      Fonte: <a href="https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error" target="_blank">Pyperclip</a>
   </p>
</details>

<details>
   <summary>
      Not Tkinter Found?
   </summary>
   <p>
      ** Microsoft Windows and Apple macOS haven't that problem because the Python Installer contains it.
   </p>
   <p>
      For Debian-based Linux: <code>sudo apt install python3-tk</code>
   </p>
   <p>
      For Fedora-based Linux: <code>sudo dnf install python3-tkinter</code>
   </p>
   <p>
      For Arch-based Distros: <code>sudo pacman -S tk</code>
   </p>
   <p>
      For RHEL, CentOS, Oracle Linux: <code>sudo yum install -y tkinter tk-devel</code>
   </p>
</details>

### Appearance
Look at the software appearance window here.

![password generator image](https://github.com/abelbcarvalho/images-software/blob/main/images/password-generator-1.png)

### The End
It's a simple project task to make an useful software.

-- *Abel Carvalho*

*That's all folks!!!*
