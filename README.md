# Sistema de Gestión de Centros Deportivos (SGCD)

Refactoring Django web app developed in 2018 for Proyecto Final assignment, at UTN FRLP.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For running your project, you first need to install Pipenv.

```
pip install pipenv
```


### Installing

Activate your Pipenv environment, and install all the dependencies

```
pipenv shell
```

```
pipenv install
```

All packages in Pipfile file should be installed, and Pipfile.lock should be updated.

## Creating an user

Explain how to run the automated tests for this system

To create a new user, you just have to be inside actions folder, and run

```
python manage.py createsuperuser
```

Follow the steps and you'll have your user for using locally. Finally, for running it, run

```
python manage.py runserver
```

## Authors

* **Ignacio Gazzaniga**
* **Martín Lucena**
* **Ulises Perez Rodriguez**
* **Iván Steger**
