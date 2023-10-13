# The AirBnB_clone - The Console ⛪


## Description 🏠
A comprehensive web application comprising database storage, a back-end API, and a front-end interface.
This console serves as our foundational stage in the development of a full-stack web application.
Its primary function is to function as a command interpreter for Airbnb objects,
allowing interactive data model manipulation, object management, and command execution.`

## The Console 
The console is a command line interpreter that permits management of the backend of AirBnB.
It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the ```storage``` object defined above).

## How It Works
The console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution of the file ```console.py``` at the command line.

## Non-Interactive Mode
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

## Interactive Mode
When using the AirBnB console in interactive mode, run the file ```console.py``` by itself:

```$ ./console.py```

While it's running in the interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```



To quit the console, the command ```quit```, or the EOF signal (```ctrl-D```) is implemented

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

## Authors: 🧠

[Hassan Olaoluwa Hakeem](https://github.com/Hassanyoung1)

[Eucharia Okoye](https://github.com/Karisma-471)
