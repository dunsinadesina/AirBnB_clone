0x00. AirBnB clone - The console
Description of the Project
This is the first step towards building a first full web application: the AirBnB clone. This first step is very important because this is what will be used build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration. This project focues on the console(backend)
description of the command interpreter:
how to start it
how to use it
examples
How to start it: The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command into an execution of the file console.py at the command line.
To run it interactively:
This should be done:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

To run it non-interactively:
This should be done:
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

How to use it:
run ./console.py, this prompt "(hbnb)" will pop out
$ ./console.py
(hbnb) 

Examples:
To quit the console, do the following:
$ ./console.py
(hbnb) quit
$

To get help on create, do the following:
$ ./console.py
(hbnb) help create
This template can be used for show, destroy, update, all, etc
