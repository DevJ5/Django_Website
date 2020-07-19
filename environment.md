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
- create templates folder + create another folder for our html files
- in settings.py add our blog app class to INSTALLED_APPS list as blog.apps.BlogConfig
- in views.py we return render(request, 'blog/home.html', context)
- the last argument of render is an object we can pass down to the template, in this case context
- use {% for post in posts %} to start for loop and {% endfor %} to end (jinja style)
- variables are accessed with doubly curly {{post.title}}
- use template blocks to reuse other templates (template inheritance)


