**Create virtual env**
virtualen django_env

**Activate virtual env**
source django_env/Scripts/activate

**Create file with all dependencies**
pip freeze --local > requirements.txt

**Version of django**
python -m django --version

**Deactivate the virutal env**
deactivate

**Start django project**
django-admin startproject djangoblog

**Run the webserver**
python manage.py runserver

**Start django app**
python manage.py startapp blog

* * *

## Steps:
- create urls.py
- create a route in views.py
- add an item to project urls.py to forward to app urls
