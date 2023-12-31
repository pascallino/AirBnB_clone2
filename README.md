# x00. AirBnB clone - The console
![Optional Text](hbnb.png)
## Background Context
***Welcome to the AirBnB clone project!***<br>
Before starting, please read the ***AirBnB*** concept page.
### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: `HTML/CSS templating`, `database storage`, `API`, `front-end integration`…<br>
#### Each task is linked and will help you to:
* put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

# 0x02. AirBnB clone - MySQL
## Background Context
Environment variables will be your best friend for this project!
* HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
* HBNB_MYSQL_USER: the username of your MySQL
* HBNB_MYSQL_PWD: the password of your MySQL
* HBNB_MYSQL_HOST: the hostname of your MySQL
* HBNB_MYSQL_DB: the database name of your MySQL
* HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
