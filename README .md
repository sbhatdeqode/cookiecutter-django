
# Cookiecutter Django Rest Framework Template.

Using this Cookiecutter template easily build your DRF app.






## Features

- Django-allauth is configured for authentication.
- Swagger documentation.
- Multiple database server options.
- Multiple CI tool option.
- Mail service configured.
- Celery-Reddis configured.
- Docker and docker-compose files added.


## Pre-Requisites

- Python 3
- Docker
## Installation

Create virtual environment with python.

```bash
  Python3 -m venv venv
```

Activate virtual environment.(Linux)

```bash
  source venv/bin/activate
```

Install cookiecutter package.

```bash
  pip install cookiecutter
```

Create project using github link

```bash
  cookiecutter gh:sbhatdeqode/cookiecutter-django
```

Then choose the option/feature you want to include in your project and your project will be created in no time.

** Do not forget add your own  variables' values in .env file.
## Running the project.

You can run the project using the docker-compose file provided.
To do that go to the project directory and run below command. 

```docker

docker-compose up -d
```

Your django app will be running at http://127.0.0.1:8000/.
