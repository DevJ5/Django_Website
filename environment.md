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
### Setup html template response
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
- create folder static/blog for statics
- {% load static %} on top of file to load static css
- use the name in urls.py for the hrefs
- set up the admin panel, first we need to set up the table in DB, python manage.py migrate
- then create superuser, python manage.py createsuperuser
### Models
- creating models for our ORM in models.py
- Generate SQL code from model: python manage.py makemigrations
- check the generated SQL: python manage.py sqlmigrate blog 0001
- run the queries against our DB: python manage.py migrate
- query the DB through the models: python manage.py shell
- register model in admin panel, in admin.py put a line: admin.site.register(Post)
### Models with shell
- import the models in the shell, from blog.models import Post, from django.contrib.auth.models import User
- get all users: User.objects.all()
- user = User.objects.filter(username='mario').first()
- user = User.objects.get(id=1)
- post_1 = Post(Post(title='In search of a princess', content='Still searching :)', author=user))
- post_1.save() 
- define dunder (double underscore) methods/magic methods like - def __str__(self):return self.title - to print Object
- user.post_set.all() and user.post_set.create(title="A", content="AAAA") immediately use the user
### Models in view
- use Post.objects.all() in context argument
- use {{ post.date_posted|date:'d M, Y' }} to format date
### Create users app for signup/login
- python manage.py startapp users
- add it to installed apps in project settings.py 'users.apps.UsersConfig'
- create a register.html view in templates/users and import UserCreationForm
- user django csrf token {% csrf_token %} and form {{form.as_p}}
- implement a one time success message in register function and base.html and redirect to home
- create a forms.py that extends UserCreationForm to add our own custom fields
- install django-crispy-forms to add custom css to our forms
- add {% load crispy_forms_tags %} to our register.html and add crispy filter to form (form|crispy)


