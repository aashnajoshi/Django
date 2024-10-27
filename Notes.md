# Django Notes (Beginner's Perspective)

## 1. Setting Up the Development Environment
### Creating a Virtual Environment with Pipenv:
- Install Pipenv:
```bash
    pip install pipenv
```
- Create a new virtual environment:
```bash
    pipenv install
```
This creates a virtual environment with the name of Base Directory followed by some random characters in *C:\Users\{user_name}\.virtualenvs* location.

### Installing Packages
- To install a package:
```bash
    pipenv install {package_name}
```
- To install all packages from an existing Pipfile containing list of packages with specific version (if mentioned), (*) means latest version available:
```bash
    pipenv install
```
### Activating the Virtual Environment
- Activate the virtual environment:
```bash
    pipenv shell
```

## 2. Packages installed and their usage:
- `pipenv`: A tool for managing virtual environments.
- `django`: A high-level Python web framework for rapid development.
- `django-debug-toolbar`: A debugging tool for Django applications.
- `pillow`: An image processing library for Python.
- `faker`: A tool for generating fake data for testing purposes.
- `uuid`: A tool for generating universally unique identifiers (UUIDs).

## 3. Creating a New Django Project
- To start a new project in the current directory:
```bash
    django-admin startproject project_name .
```
- After *manage.py* is created, use:
```bash
    python manage.py <command>
```

## 4. Running the Development Server
- Start the Django development server:
```bash
    python manage.py runserver
```

## 5. Creating a Django App
- Create a new app:
```bash
    python manage.py startapp app_name
```
- Add `app_name` to `INSTALLED_APPS` in *project_name/settings.py*.

## 6. Database Migrations
### Registering Models in Admin
- Add your model to *app_name/admin.py*:
```python
    from .models import ModelName
    admin.site.register(ModelName)
```

### Steps to Make Migrations
1. Create or update the database after changes in *app_name/models.py*:
```bash
    python manage.py makemigrations
```
2. View the SQL for a specific migration (optional):
```bash
    python manage.py sqlmigrate app_name mig_no
```
- The migration_no. can be seen as output to first command or manually by checking in *app_name/migrations* directory. (This step is only necessary if you want to migrate a specific version, else we can simply migrate and the latest file would be migrated)

3. Apply migrations:
```bash
    python manage.py migrate
```

4. Delete table from database:
```bash
    python manage.py makemigrations -n drop_all_tables app
```

- Apply the delete action:
```bash
    python manage.py migrate app
```

- Delete the *app_name/migrations* directory and the `db.sqlite3` file.

- Run the migrations (Step 1 & 3) again to create the tables again.

## 7. CRUD Operations
- Open the shell:
```bash
    python manage.py shell
```
### Adding Data
- Add data:
```python
    from app.models import *
    ModelName.objects.create(field = "entry", field2 = entry2...)
```
            OR
```python
    from app.models import *
    data = ModelName(field = "entry", field2 = entry2....)
    data.save()
```
            OR
```python
    from app.models import *
    data_dict = {"field1": "entry", "field2": "entry2"} #For dictionary or JSON format data
    ModelName.objects.create(**data_dict)
```

- Here, we imported all models in *app_name/models.py*, where `name` determines the class_name of the schema we defined.

### Reading Data
- Fetch all entries:
```python
    from app.models import *
    data = ModelName.objects.all()
    for d in data:
        print(f"The data stored is {d.field1}: {d.field2}")
```
- Fetch a specific entry:
```python
    info = ModelName.objects.get(id = 2) 
    print(info) # Print the data saved in id 2, if id doen't exist it would throw an error
```
- The *id* field is automatically created by django for referencing data. To bypass the error, we can use: *name.objects.filter(id = )*, if id doesn't exist it would return an empty string else return the object of given id.

### Updating Data
- Update an entry:
```python
    from app.models import *
    data = ModelName.objects.get(id=2)
    data.field1 = "new_entry"
    data.save()
```
            OR
```python
    from app.models import *
    ModelName.objects.filter(id = 2).update(field1 = "new_entry") 
```

### Deleting Data
- Delete an entry:
```python
    ModelName.objects.get(id=2).delete() # To delete a specific entry
    Modelname.objects.all().delete()  # To delete whole data
```

- then *python manage.py flush*

## 8. Admin Panel
- Create a superuser:
```bash
    python manage.py createsuperuser
```
- Once username and password are created (email optional). Access the admin panel at *http://localhost:8000/admin* and login via same credentials!

## 9. Handling Media Files
### Adding Images/Files
- Install Pillow:
```bash
    pipenv install Pillow
```
- Define fields in *app_name/models.py*:
```python
    models.ImageField(upload_to='uploads/', null=True, default=None)
```
- Configure *project_name/settings.py*:
```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
```
- Update *project_name/urls.py*:
```python
    from django.conf import settings
    from django.conf.urls.static import static

    #After URL_PATTERNS, add the following lines:
    if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 10. Sending Emails
- Configure email settings in *project_name/settings.py*:
```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'your_email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your_email_password'
    EMAIL_USE_TLS = True
```
- Adding logic into *app_name/views.py*:
```python
    from django.contrib import messages
    from django.core.mail import EmailMessage
    from django.conf import settings

    def send_email(request):
        if request.method == 'POST':
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            recipient_list = [email.strip() for email in request.POST.get('recipients').split(',')]
            file_path = request.FILES.get('file_path')  # Optional

            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            
            if file_path:
                email.attach(file_path.name, file_path.read(), file_path.content_type)

            if email.send():
                messages.success(request, 'Mail sent successfully!')
            else:
                messages.error(request, 'Failed to send mail. Please try again.')

            return redirect('send_email')
        else:
            return render(request, 'index.html', context={'mail': 'mail'})
```

- Then in *app_name/urls.py*, add the following lines:
```python
    urlpatterns = [
        path('send_email/', views.send_email, name='send_email'),
    ]
```
## 11. Django Signals
- Django signals allow you to perform automatic actions in response to model changes, such as creating logs. 

### Common Signal Types
- `post_save`: Triggered after a model instance is saved.
- `pre_save`: Triggered just before a model instance is saved.
- `post_delete`: Triggered after a model instance is deleted.
- `pre_delete`: Triggered just before a model instance is deleted.

- Usage:
```python
    from django.db.models.signals import post_save
    from django.dispatch import receiver

    @receiver(post_save, sender=ModelName)
    def my_handler(sender, instance, **kwargs):
        # Code to execute after the model instance is saved
```

- `my_handler` function is called each time the `post_save` condition is met, such as when a new model instance is created.

## 12. Tailwind CSS Integration
- Install Tailwind:
```bash
    pipenv install django-tailwind
```
- Configure Tailwind:
```bash
    python manage.py tailwind init theme
```
- Now a new directory named *theme* is created in BASE_DIR which contains all the designs and layouts using which we can use. Before that in *app_name/settings.py*:
```python
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r"C://Program Files//nodejs//npm.cmd"
```
- Add *theme* to INSTALLED_APPS.

- Now run the following command to finally install.
```bash
    python manage.py tailwind install
```

### Running the Application
- Use two terminals:
    - For the Django server:
```bash
    python manage.py runserver
```
    - For Tailwind:
```bash
    python manage.py tailwind start
```

## 13. Using Django ORM (Raw SQL in Django):

### Using `connection`:
    - `connection.cursor()`: Execute raw SQL queries.
    - `connection.commit()`: Commit the changes.
    - `connection.rollback()`: Roll back the changes.

- Usage:
```python
    from django.db import connection
    from django.db import transaction

    @transaction.atomic
    def add_entry(name, description):
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO ModelName (name, description) VALUES (%s, %s)", [name, description])
```
- Use of `django.db import transaction`: To implement the Atomicity property of the database, meaning operations are completed fully or not at all.

### Using `RawSQL`:
    - `RawSQL(query, params)`: Execute raw SQL queries with parameters.
    - `RawSQL(query, params, output_field=None)`: Execute raw SQL queries with parameters and specify an output field.

- Usage:
```python
    from django.db.models import RawSQL
    from django.db import models

    class ModelName(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

    def add_entry(name, description):
        query = f"INSERT INTO ModelName (name, description) VALUES {name, description}"
        RawSQL(query, [name, description]).execute()
```

- __Comparision__: Using `connection` provides direct control over database operations and is suited for complex queries, while `RawSQL` is better for integrating raw SQL within Django’s ORM when you need to execute parameterized queries without managing database connections directly.