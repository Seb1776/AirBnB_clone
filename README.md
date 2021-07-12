![github](https://camo.githubusercontent.com/8395fcb11f752cada62206146c4cd905232e850c472d2c16213cd6825a9925ff/68747470733a2f2f692e696d6775722e636f6d2f7378766257674f2e706e67)


# <h1 align="center">:file_folder: AirBnB clone - The console</h1>

The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://intranet.hbtn.io/rltoken/FrRTcvuF5L9wWDzFE9k01A).

Our application will be composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell
* A website that shows the final: static and dynamic
* A database or files that store data
* An API that provides a communication interface between the front-end and our data
# First step: Write a command interpreter to manage your AirBnB objects.
![AirBnB_Structure](https://camo.githubusercontent.com/e6b2a27106509da1964c97ca9a270489f85862a3222d4de27a58870b33daeeae/68747470733a2f2f692e6962622e636f2f34323563704e4c2f434143412e706e67)

In the previous image we can see the struct of all our project with Airbnb, we done the first part of this that is the console, this console is made for the developer, here we can manage the commands:

```
👉 create
👉 update
👉 show
👉 all
👉 destroy
```
## Our classes 🙌🏻
- State: 🌆
   - Public class attributes:
     - name: will be the name of teh state to
- City: 🏙
   - Public class attributes:
     - state_id: string - empty string: it will be the State.id
     - name: string - empty string
- Amenity : ⭐️
   - Public class attributes:
   - name: string - empty string
- Place: 🌎
  - Public class attributes:
     - city_id: string - empty string: it will be the City.id
     - user_id: string - empty string: it will be the User.id
     - name: string - empty string
     - description: string - empty string
     - number_rooms: integer - 0
     - number_bathrooms: integer - 0
     - max_guest: integer - 0
     - price_by_night: integer - 0
     - latitude: float - 0.0
     - longitude: float - 0.0
     - amenity_ids: list of string - empty list: it will be the list of Amenity.id later
- Review: ✅
   - Public class attributes:
     - place_id: string - empty string: it will be the Place.id
     - user_id: string - empty string: it will be the User.id
     - text: string - empty string

This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

### :stop_sign: Each task is linked and will help you to:

- [x] put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- [x] create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- [x] create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- [x] create the first abstracted storage engine of the project: File storage.
- [x] create all unittests to validate all our classes and storage engine

# ***Example of use:***

# :desktop_computer: The command interpreter < ***Execution*** >

### Non-interactive mode: ```$ echo <command> | ./console.py ```
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
### Interactive mode: ```$ ./console.py```

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
---
###  <h2 align="center">By:  Sebastian Toro :man_technologist: & Jorge Armando Morales :man_technologist:</h2>
---