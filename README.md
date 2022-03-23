![alt text](https://www.dropbox.com/s/rw7t5n9etbkimul/Screenshot%20from%202022-03-23%2006-50-43.png?raw=true)

# Service@MyBranch

## Table of Contents
* [Introduction](#introduction)
* [Installation](#installation) 
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Contributors](#contributors)
* [License](#license)

## Introduction

This is a project that offers customers of a bank the platform to express their
satisfactions and express their unsatisfactions. The platform is deployed [here](https://rmatovu987.github.io/service-mybranch/).

## Installation

The project is built using [Angular 13](https://angular.io/) and [Python 3](https://www.python.org/downloads/).
In order to run the Angular project, you need to install [node](https://nodejs.org/en/). Then, cd into the Angular
project and run

```bash
npm install
```

This will install all the required node modules. Afterwards, run

```bash
ng serve
```

## File Descriptions
#### `backend/` directory contains all backend features of the project.
These include:
* `models/` - a directory for all the project models
* `tests/` - a directory for all the tests using python unittests
* and the storage `engine/` - defines the storage structure of the project
### `backend/models` This directory contains the model classes used in this project.
[base_model.py](backend/models/base_model.py) - The BaseModel class from which all other classes are derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `update` with the current datetime 
* `def to_dict(self)` - returns a dictionary representation of the instance
* `def delete(self)` - delete current instance from storage

Classes that inherit from Base Model:
* [bank.py](backend/models/bank.py) - defines the bank class
* [branch.py](backend/models/branch.py) - defines the bank branch class
* [review.py](backend/models/review.py) - defines the review class
* [user.py](backend/models/user.py) - defines the user class

#### `backend/models/engine` directory contains File Storage class that handles JASON serialization and deserialization:
* [file_storage.py](backend/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* [db_storage.py](backend/models/engine/db_storage.py) - defines the database storage engine

### `backend/models/tests`
#### `tests/test_models` - a directory for each model's unittests
* [test_base_model.py](backend/tests/test_models/test_base_model.py) - unittests for the BaseModel
* [test_bank.py](backend/tests/test_models/test_bank.py) - unittests for the bank model
* [test_branch.py](backend/tests/test_models/test_branch.py) - unittests for the branch model
* [test_review.py](backend/tests/test_models/test_review.py) - unittests for the review model
* [test_user.py](backend/tests/test_models/test_user.py) - unittests for the user model

#### `tests/test_engine` - unittests for the storage engine

## Usage

## Contributors

This project is an effort of:
    - [Richard Matovu](https://github.com/rmatovu987)
    - [Promise Emmanuel Yehangane](https://github.com/nuel07)

## License

[MIT](https://choosealicense.com/licenses/mit/)
