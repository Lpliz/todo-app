## ToDo Class
The attributes of ToDo Class is:

    title : String
    description : String
    created_at : DateTime Auto
    updated_at : DateTime Auto

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

    a) Add a new ToDo:- http://127.0.0.1:8000/todo/add (POST with ToDo Object attributes in JSON)
    b) Display list of ToDo:- http://127.0.0.1:8000/todo/display (GET)
    c) Edit a particular ToDo:- http://127.0.0.1:8000/todo/edit/<int:pk> (PUT with ToDo Object attributes in JSON)
    d) Delete a particular ToDo:- http://127.0.0.1:8000/todo/delete/<int:pk> (DELETE)
    e) Delete all ToDo Tasks:- http://127.0.0.1:8000/todo/deleteAll (DELETE)
