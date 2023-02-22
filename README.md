# INCIDENT-MANAGEMENT-SYSTEM

crud_api with signup and login

using simple jwt authentication

Admin user :- incident@gmail.com Admin password :- 1234

At first clone this project- Install this module :- pip install virtualenv Then create virtual env. in which directory your project is cloned usig this command :- virtualenv venv Then activate your virtual env after your dir :- .\venv\Scripts\activate. Then go to project folder and run this command :- pip install -r requirements.txt.

Then run this command to run the project :- python manage.py runserver

Then....

POST http://127.0.0.1:8000/incident/signup/ responsible for signup with name,email,mobile and password with post method. POST http://127.0.0.1:8000/incident/login/ responsible for signin with email and password and return a valid token with post method. GET http://127.0.0.1:8000/incident/getuser/ get all user whaterever users created.

Thanks................
