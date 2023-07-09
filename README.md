## Project Description
This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

### How to use:
Execute:
      ```
        ./console.py
      ```
### Commands: 📄

| Command | Example    | Description                       |
| :-------- | :------- | :-------------------------------- |
| `create`      | `create User` | Creates a new instance, print its **`id`** |
| `show`      | `show BaseModel 'valid_id'` /  `BaseModel.show("'valid_id'")` | Prints the string representation of an instance |
| `destroy`      | `destroy City 'valid_id'` / `City.destroy("'valid_id'")`| Deletes an instance |
| `all`      | `all` / `all User` /  `User.all()`| Prints all string representation of all instances |
| `update`      | `update BaseModel 'valid_id' email "aibnb@mail.com"` / `BaseModel.update("'valid_id'", "email", "aibnb@mail.com")` / `BaseModel.update("'valid_id'", {'email' : "aibnb@mail.com", 'age': 23})`|  Updates an instance |
| `help`      | `help` /  `help Create`|  Help |
| `quit`      | `quit` |  Exit the program |

#### Supported Classes:
```
BaseModel, User, State, City, Amenity, Place, Review
```

## How to use it
It can work in two different modes:


**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

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

In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


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

## Authors

- [@Washx23](https://github.com/Washx23)
- [Coxan33] (https.//github.com/Coxan33)
