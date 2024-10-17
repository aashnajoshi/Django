# Creating a virtual env using pipenv
```bash
pipenv install {package_name}
```

# To activate virtual env created while creating the dir
```bash
pipenv shell
```

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

# To create users we first need to create a super-user that can be done using:
```bash
python manage.py createsuperuser
```

# To configure tailwind (if needed):
```bash
pipenv install django-tailwind 'django-tailwind[reload]'
```

- Once installed, we add *tailwind* to INSTALLED_APPS (in *settings.py*) and then initialize tailwind
```bash
python manage.py tailwind init theme
``` 

- Now a new directory named *theme* is created which contains all the designs and layouts using which we can use. Before that add these into *settings.py*:
    - create new variable called TAILWIND_APP_NAME = 'theme'
    - add *theme* to INSTALLED_APPS.
    - create a new variable called NPM_BIN_PATH = r"C://Program Files//nodejs//npm.cmd"

Now run the following command to finally install.
```bash
python manage.py tailwind install
```

- From now on we will use two terminals one for *python manage.py runserver* and another for *python manage.py tailwind start*

# To take images in db:
- We use *models.ImageField(upload_to = 'location/for/saved/image')* in models.py
- We then need to install Pillow library for image processing
- Then in settings.py:
    - MEDIA_URL = '/media/'
    - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
- Then in project's urls.py:
    - from django.conf import settings
      from django.conf.urls.static import static
