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
- define dunder (double underscore) methods/magic methods like - def __str__(self):return self.title - to print object
- user.post_set.all() and user.post_set.create(title="A", content="AAAA") immediately use the user
### Models in view
- use Post.objects.all() in context argument
- use {{ post.date_posted|date:'d M, Y' }} to format date
### Create users app for signup
- python manage.py startapp users
- add it to installed apps in project settings.py 'users.apps.UsersConfig'
- create a register.html view in templates/users and import UserCreationForm
- user django csrf token {% csrf_token %} and form {{form.as_p}}
- implement a one time success message in register function and base.html and redirect to home
- create a forms.py that extends UserCreationForm to add our own custom fields
- install django-crispy-forms to add custom css to our forms
- add {% load crispy_forms_tags %} to our register.html and add crispy filter to form (form|crispy)
### Login
- auth_views.LoginView.as_view(template_name='users/login.html'), handles the login logic for us
- still have to create a login template (use cripsy forms again)
- logging in will redirect default to account/profile, change this in settings: LOGIN_REDIRECT_URL = 'blog-home'
- add a profile view that renders profile.html
- add @login_required annotation
- in settings add LOGIN_URL = 'login' otherwise going to profile when logged out, will redirect to accounts/login
### Profile model with image
- create a profile model to extend our user model with a profile picture (user doesnt have that)
- use OneToOneField and ImageField
- python manage.py makemigrations and then do them with python manage.py migrate
- to view/create the profiles on admin page, register this Profile model in admin.py
- add a MEDIA_ROOT and MEDIA_URL in settings.py where the images will go, otherwise they will default to a root folder
- {{user.profile.image.url}} to use the image
- to serve the image file in development we can add if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
- For production this needs to be different, look up in django docs
- drop a default.jgp image in the media folder
### Signal to create a profile upon user creation
- make file signals.py
- use @receiver(post_save, sender=User) decorator. When a User is saved send post_save signal, this signal is received by the receiver and this receiver runs create_profile function
- it also needs to be saved, so create another @receiver function named save_profile
- **kwargs is just any amount of keyword arguments
- Finally in users apps.py in the UsersConfig add a method ready that imports the users.signals
### Update user profile
- create 2 new form function in forms.py
- set multipart/formdata for the profile picture and use request.FILES
- to resize the uploaded picture to a thumbnail use Pillow (PIL)
- overwrite the save method: call its super and then resize image
### Class based list view and detail view
- in views.py create class based views that inherit ListView/ DetailView
- add them to urls.py
- for detail view use integer primary keys in the path, path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')
- Django automatically looks at <model>_detail.html for the template
- use object as variable in detail template
### Create Posts
- create a url pattern 
- First create a PostCreateView class that inherits CreateView
- the default template name for this is post_form.html, this will be the same for an UpdateView
- then overwrite the super is_valid() method to add the logged in User FK as author
- then after POST request is done, we need a redirect to this post. Use get_absolute_url for that in our model
- use reverse instead of redirect, reverse makes sure that we get the id correct
- we cant use login require annotation on classes, so we use a mixin instead: LoginRequiredMixin
### Update Posts
- create url pattern: path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update')
- create a view PostUpdateView
- set it up so only authorized users can update with a UserPassesTestMixin
- test_func() should return True if self.request.user == post.author
- this update view uses the same post_form.html
### Delete Posts
- create url pattern: path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
- create a view PostDeleteView
- set up authorization and login mixins
- add a test_func
- add a success_url for redirection after deletion
- use template called post_confirm_delete
### Add buttons to delete/update routes
- add an if statement if the user == object.author
- add buttons that take the object id as argument
### Pagination
- from django.core.paginator import Paginator
- set paginate_by attribute
- create first, previous, some pages in the middle, next, last buttons with some simple for loop and if statements
- create a class view (with get_queryset) and a template page for the posts by a certain user
### Reset password email
- set up environment variable for username, password
- in setttings add smtp server, port, username, password, tls enabled
- add template for password_reset -> password_reset_done -> password_reset_confirm -> password_reset_complete 
- care for _ and - in url patterns



