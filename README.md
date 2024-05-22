# My Django Project

This is a simple Django project "To-do list" that demonstrates how to create and run a Django application locally.

## Installation & Run
### Set up the environment 


 On Windows:
```python
python -m venv venv 
venv\Scripts\activate
 ```

 On UNIX or macOS:
```python
python3 -m venv venv 
source venv/bin/activate
 ```

### Install requirements 
```python
pip install -r requirements.txt
```


### Database setup

```python
python manage.py migrate
```

### Install database fixture
```python
python manage.py loaddata db.json
```


### Create a superuser (optional)
If you want to create a superuser account for accessing the Django admin panel, run:
```python
python manage.py createsuperuser
```

### Run the project
```python
python manage.py runserver
```
### Go to site [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
