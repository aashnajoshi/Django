# Creating a virtual env using pipenv
```bash
pipenv install {package_name}
```

# To activate virtual env created while creating the dir
```bash
pipenv shell
```

# Packages installed and their usage:
- `pipenv`: A tool for managing virtual environments.
- `django`: A high-level Python web framework for rapid development.
- `django-debug-toolbar`: A debugging tool for Django applications.
- `pillow`: An image processing library for Python.
- `faker`: A tool for generating fake data for testing purposes.

# To start a new django project in cwd (.)
```bash
django-admin startproject project_name .
```
Once the manage.py is created we don't need to call *django-admin* to run tasks we can simply use python manage.py to get same results

# To run a django server 
```bash
python manage.py runserver
```

# To create a django app
```bash
python manage.py startapp app_name
``` 
After creating the app we need to add the *app_name* inside settings.py (in project_name) > INSTALLED_APPS

# Managing Database Migrations in Django is a three-step process:
- To create or update your database after making changes to the *models.py* file in the *app_name* directory, follow these steps:
```bash
python manage.py makemigrations
```

- If you want to see the SQL that will be executed for a specific migration, you can run (OPTIONAL):
```bash
python manage.py sqlmigrate app_name mig_no
```
The migration_no. can be seen as output to first command or manually by checking the *migrations* directory inside *app_name* directory. (This step is only necessary if you want to migrate a specific version, else we can simply migrate and the latest file would be migrated)
 
- Finally, apply the migrations to your database with:
```bash
python manage.py migrate
```

- Oh, one more thing, register the *model* by adding it to *admin.py* file, where *model_name* is the name of class you used in *models.py* file:
```bash
from .model import model_name
admin.site.register(model_name)
```

- To delete entries from database:
```bash
python manage.py makemigrations -n drop_all_tables app
```

- Apply the delete action:
```bash
python manage.py migrate app
```

# To ADD data in schema:
```bash
python manage.py shell
```

- The above command opens an interactive interpretor, to add data now we will simply import our model and add data:
```bash
from app.models import *
name.objects.create(field = "entry", field2 = entry2...)
```
            OR
```bash
from app.models import *
data = name(field = "entry", field2 = entry2....)
data.save()
```
            OR
```bash
from app.models import *
data_dict = {"field1": "entry", "field2": "entry2"} #For dictionary or JSON format data
name.objects.create(**data_dict)
```

- Here, we imported all models in *models.py* from our *app*, where *name* determines the class_name of the schema we defined inside *models.py* file.

# To READ data from schema:
```bash
from app.models import *
data = name.objects.all()
data # The format of data printed depends on the structure returned by __str__ in models.py

for d in data:
print(f"The data stored is {d.field1}: {d.field2}") # Or in any format you want

info = name.objects.get(id = 2) 
print(info) # Print the data saved in id 2, if id doen't exist it would throw an error
```
- The *id* field is automatically created by django for referencing data. To bypass the error, we can use: *name.objects.filter(id = )*, if id doesn't exist it would return an empty string else return the object of given id.

# To UPDATE the data in schema:
```bash
from app.models import *
data = name.objects.get(id = 2) # Target the data saved in id 2
data.field1 = "new_entry"
data.save()
```
            OR
```bash
from app.models import *
name.objects.filter(id = 2).update(field1 = "new_entry") 
```

# To DELETE the data from schema:
```bash
from app.models import *
name.objects.get(id = 2).delete()  # To delete a specific entry
name.objects.all().delete()  # To delete whole data
```
then *python manage.py flush*

# To access Django's Admin Pannel, we first need to create a super-user using:
```bash
python manage.py createsuperuser
```

- Once username and password are created (email optional) we can go to *http://localhost:8000/admin* and login via same credentials!

# To add images/files in db:
- We then need to install Pillow library for image processing: *pipenv install Pillow*

- For images, we use: *models.ImageField(upload_to = 'location/wrt/BASE_DIR', null=True, default=None)*. Similarly for files, we use: *models.FileField()* in *models.py* file.

- Then in settings.py:
```bash
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- Then in urls.py:
```bash
from django.conf import settings
from django.conf.urls.static import static
```

- After URL_PATTERNS, add the following line:
```bash
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

# To send mail using django:
- First install *pipenv install django-allauth*

- Then in *settings.py*, add the following lines:
```bash
INSTALLED_APPS += ['allauth', 'allauth.account', 'allauth.socialaccount']
EMAIL_BACKENDS = 'django.core.mail.backends.smpt.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
```

- Then in *utils.py*, add the following code:
```bash
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

subject = ""
message = ""
from_email = settings.EMAIL_HOST_USER
recipient_list = [""]

def mail_sender(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)

def mail_with_attach(subject, message, recipient_list, file_path):
    email = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    email.attach_file(file_path) 

```

- Then in *views.py*, add the following lines:
```bash
from .utils import mail_sender

def send_email(request):
    mail_sender()
    return redirect('/')
```

- Then in *urls.py* in *app_name* directory, add the following lines:
```bash
from django.urls import path
from .views import send_email



# To configure tailwind (if needed):
```bash
pipenv install django-tailwind 'django-tailwind[reload]'
```

- Once installed, we add *tailwind* to INSTALLED_APPS (in *settings.py*) and then initialize tailwind
```bash
python manage.py tailwind init theme
``` 

- Now a new directory named *theme* is created which contains all the designs and layouts using which we can use. Before that add these into *settings.py*:
    - Create new variable called TAILWIND_APP_NAME = 'theme'
    - Add *theme* to INSTALLED_APPS.
    - Create a new variable called NPM_BIN_PATH = r"C://Program Files//nodejs//npm.cmd"

- Now run the following command to finally install.
```bash
python manage.py tailwind install
```

- From now on, we will use two terminals: one for *python manage.py runserver* and another for *python manage.py tailwind start*