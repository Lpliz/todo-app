# Instructions to Run
## 1. Install dependencies:
    pip install django djangorestframework 
## 2. Configure database in your Django settings
## 3. Setup the database and run migrations:
    python manage.py makemigrations
    python manage.py migrate
## 4. Run the Django development server:
    python manage.py runserver
## 5. Run test cases:
    python manage.py test
## 6. Invoke the APIs as:
After running the server, each API can be independently called using following API endpoints:

    a) Add a new ToDo:- http://127.0.0.1:8000/todo/add
    b) Display list of ToDo:- http://127.0.0.1:8000/todo/display
    c) Edit a particular ToDo:- http://127.0.0.1:8000/todo/edit/<int:pk>
    d) Delete a particular ToDo:- http://127.0.0.1:8000/todo/delete/<int:pk>
    e) Delete all ToDo Tasks:- http://127.0.0.1:8000/todo/deleteAll 
