# Sistema de Gestión de Centros Deportivos (SGCD)

Refactoring Django web app developed in 2018 for Proyecto Final assignment, at UTN FRLP.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For running your project, you first need to have Python 3.8 installed in your system
Then, install Pipenv.

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

To create a new user, first you have to apply migrations. Just run:

```
python manage.py migrate
```

After they're all applied:

```
python manage.py createsuperuser
```


For loading some initial data, run

```
make load_all_fixtures
```

Finally, run with:

```
python manage.py runserver
```

## Authors

* **Ignacio Gazzaniga**
* **Martín Lucena**
* **Ulises Perez Rodriguez**
* **Iván Steger**
