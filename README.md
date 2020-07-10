```
██╗      ██████╗ ██╗  ██╗██████╗
██║     ██╔═══██╗██║ ██╔╝██╔══██╗
██║     ██║   ██║█████╔╝ ██████╔╝
██║     ██║   ██║██╔═██╗ ██╔══██╗
███████╗╚██████╔╝██║  ██╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
```

# LOKR

![logo](https://raw.githubusercontent.com/BugsForDays/Lokr/master/Lokr/assets/closedlock.ico)

## SecureLocker Improved. A little bit safer. New GUI. Edit and Delete Passwords

### VERSION 1.2

### Created by [petabite](https://github.com/petabite "To my Github Profile!!!") aka 尸廾工𠃊工尸 乙

---

---

---

## CHANGELOG:

| Release | Changes                                                                                                 |    Date    |
| :-----: | :------------------------------------------------------------------------------------------------------ | :--------: |
|  v1.2   | <ul><li>fix resolving resource path bug</li><li>support for running w/o invoking python</li></ul>       |  7/9/2020  |
|  v1.1   | <ul><li>Complete code refactoring</li><li>Fix .exe bugs</li><li>Reorganization under the hood</li></ul> |  8/9/2019  |
|  v1.0   | <ul><li>FIRST RELEASE!!</li></ul>                                                                       | 11/24/2017 |

## SCREENSHOT:

![screenshot](https://raw.githubusercontent.com/petabite/Lokr/master/images/screenshot.png)

---

## INSTALLATION INSTRUCTIONS:

1. Go to the releases tab in this repo.
2. For Windows: Download the Lokr.exe.zip file

   For other systems: Download the source code

   NOTE: Source Code folders contain the Python script for the program. You will need a Python interpreter in order to run.

3. Unzip the folder Lokr/Source Code folder to any location.
4. Create a shortcut if you wish for easier access(Windows only) or [write a script](https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script)(Linux) or create an Automator app that runs that script automatically(macOS)
5. Follow 'GETTING STARTED' instructions below.

---

## UPDATE INSTRUCTIONS:

1. Go to releases tab in this repo and click on the latest release.
2. For Windows: Download the Lokr.exe.zip file

   For other systems: Download compatible Source Code for your system.

   NOTE: Source Code folders contain the Python script for the program. You will need a Python interpreter in order to run.

3. Unzip the folder Lokr/Source Code folder to any location.
4. Move .exe or .py files to your current Lokr folder(the one from your very first installation) and _replace_ the old program.

   NOTE: Be careful to not replace the .lokrdata directory!!

5. Make sure to create a new shortcut(Windows).

---

## GETTING STARTED:

1. Run `python3 Lokr.py` in the Lokr directory(macOS/Linux) or double click on the Lokr icon(Windows) or run your Automator app(macOS).
2. Register an account
3. Login with new info
4. Encrypt a new password
5. Enjoy your new password manager!

---

## TROUBLESHOOTING:

### Problem:

My passwords do not show up!

### Solution:

Make sure the .lokr file associated with your account is in the .lokrdata directory. The .lokrdata directory also has to be in the same directory as the Lokr program.

### Problem:

My username and passwords are incorrect!

### Solution:

First, double check that the username and password info is correct. If that is all correct, make sure that the usrs.ulockr file is in the .lokrdata directory, which should be in the same directory as the Lokr program.

---

### DEFAULT TESTER ACCOUNT:

usrname: c

pwd: c
