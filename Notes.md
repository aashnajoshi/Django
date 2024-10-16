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
Once the manage.py is created we don't need to call "django-admin" to run tasks we can simply use python manage.py to get same results

# To run a django server 
```bash
python manage.py runserver
```

# To create a django app
```bash
python manage.py startapp app_name
``` 
After creating the app we need to add the 'app_name' into the settings.py (in project_name) > INSTALLED_APPS

# Managing Database Migrations in Django is a three-step process:
- To create or update your database after making changes to the `models.py` file in the `app_name` directory, follow these steps:
```bash
python manage.py makemigrations
```

- If you want to see the SQL that will be executed for a specific migration, you can run (optional):
```bash
python manage.py sqlmigrate app_name mig_no
```
The migration_no. can be seen as output to first command or manually by checking the 'migrations' directory inside 'app_name' directory. (the 2nd step is only necessary if you want to migrate a specific version else we can simply migrate and the latest file would be migrated)
 
- Finally, apply the migrations to your database with:
```bash
python manage.py migrate
```

- Oh, one more thing, register the 'model' by adding it to 'admin.py' file, where model_name is the name of class you used in models.py file:
```bash
from .model import model_name
admin.site.register(model_name)
```

# To create users we first need to create a super-user that can be done using:
```bash
python manage.py createsuperuser
```