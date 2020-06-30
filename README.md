# AirBnB Clone - The Console

![Holberton Logo](https://www.holbertonschool.com/holberton-logo.png)
![AirBnB Logo](https://storage.googleapis.com/www-paredro-com/uploads/2019/03/El-logo-de-Airbnb-es-el-si%CC%81mbolo-de-la-gente-lugares-amor-y-un-22A22.jpg)

# Project
In the next few months, in Holberton School, we will be creating a clone of the AirBnB app. In this repo you will find the first step towards building a full clone of this platform, which is the console. The console is the most important part of the back-end side of the clone. It will be written in Python.

# The Console
This part of the project consists in doing a command inerpreter. This command interpreter is limited to a specific use-case. In this case the command interpreter will be able to manage the objects of our project:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

# Example Usage

The command interpreter can work in two different modes: Interactive and Non-Interactive mode.

### Interactive Mode
In this mode, the console will display the prompt hbnb, which will indicate to the user that he/she can write and execute a command. After the command is executed, the prompt will appear again waiting for a new command.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode
In this mode, is requiered that the shell is runned with a command input piped into the execution. This in order to make that the command runs as soon as the shell starts. Take into account that in this mode the prompt will not appear.

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

# Authors & Contact Information
- Danilo Romero - GitHub: https://github.com/daniloromero
- Juan José Villegas - GitHub: https://github.com/juanjo7890
