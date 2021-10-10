# Django seed project with JWT authentication

This is a djangorestframework based template rest backend with JWT token authentication and basic user management already done. This created to reduce the amount of time writing in boilerplate code. The JWT authentication is done with djangorestframework-jwt library. To make use of this, you first need cookiecutter. Yoou can install it with pip
```sh
pip install cookiecutter
```
After that run,
```sh
cookiecutter https://github.com/ebin7joseph/JWT-Token-Auth-Django-Seed.git
```
It will prompt you for some inputs like project name and author name. Enter those values and the project is setup.
You have to run the following commands to setup the database.
```sh
python manage.py makemigrations
python manage.py migrate --run-syncdb
```
Run the below command for running tests.
```sh
python manage.py test
```
Run the below command to start running the server locally.
```sh
python manage.py runserver
```
