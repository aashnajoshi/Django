# Django Notes (Beginner's Perspective)

## 1. Setting Up the Development Environment
### Creating a Virtual Environment with Pipenv:
- Install: `pip install pipenv`
- Create a new virtual environment:
```bash
    pipenv install
```
- This creates a virtual environment with the name of Base Directory followed by some random characters inside: *C:\Users\{user_name}\.virtualenvs*

### Installing Packages
```bash
    pipenv install {package_name}
```
- To install all packages from an existing Pipfile containing list of packages with specific version (if mentioned), (*) means latest version available:
```bash
    pipenv install
```

### Activating the Virtual Environment
```bash
    pipenv shell
```

## 2. Packages installed and their usage:
- `pipenv`: A tool for managing virtual environments.
- `django`: A high-level Python web framework for rapid development.
- `razorpay`: A tool for secure Payment Gateway integration.

- `django-debug-toolbar`: A debugging tool for Django applications.
- `tinymce`: A rich text editor for web applications.

- `pillow`: An image processing library for Python.
- `faker`: A tool for generating fake data for testing purposes.
- `uuid`: A tool for generating universally unique identifiers (UUIDs).

## 3. Creating a New Django Project
- To start a new project in the cwd (.):
```bash
    django-admin startproject project_name .
```
- After *manage.py* file is created, now we use:
```bash
    python manage.py <command>
```

## 4. Running the Development Server (in Terminal)
- Start the Django development server:
```bash
    python manage.py runserver
```
- If we want to runserver at a specific port then: 
```bash
    python manage.py runserver 3000
```

## 5. Creating a Django App
- Create a new app:
```bash
    python manage.py startapp app_name
```
- Add `app_name` to `INSTALLED_APPS` variable in *project_name/settings.py*.

## 6. Database Migrations
### Registering Models in Admin
- Edits in *app_name/admin.py*:
```python
    from .models import ModelName
    admin.site.register(ModelName)
```

### Steps to Make Migrations (in Terminal)
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
- Run the migrations (Step 1 & 3) again to recreate the tables.

## 7. CRUD Operations
- Open the shell:
```bash
    python manage.py shell
```
### Adding Data (Create)
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
    data_dict = {"field1": "entry", "field2": "entry2"} #For dict or JSON data
    ModelName.objects.create(**data_dict)
```
- Here, we imported all models in *app_name/models.py*, where `ModelName` determines the class_name of the schema we defined.

### Reading Data (Read)
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
    print(info) #Data with id 2, if it doesn't exist it would throw an error.
```
- The *id* field is automatically created by django for referencing data. To bypass the error, we can use: *ModelName.objects.filter(id = )*,in this case if the id doesn't exist it would return an empty string else return the object of given id.

### Updating Data (Update)
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

### Deleting Data (Delete)
```python
    ModelName.objects.get(id=2).delete() # To delete a specific entry
    Modelname.objects.all().delete()  # To delete whole data
```
- Then run: *python manage.py flush*

## 8. Admin Panel
- Create a superuser:
```bash
    python manage.py createsuperuser
```
- Once username and password are created (email optional). Access the admin panel at *http://localhost:8000/admin* and login via same credentials!

## 9. Handling Media Files
### Adding Images/Files
- Install: `pipenv install Pillow`
- Edits in *app_name/models.py*:
```python
    models.ImageField(upload_to='uploads/', null=True, default=None)
```
- Edits in *project_name/settings.py*:
```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
```
- Edits in *project_name/urls.py*:
```python
    from django.conf import settings
    from django.conf.urls.static import static

    #After 'urlpatterns', add the following lines:
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 10. Sending Emails
- Edits in *project_name/settings.py*:
```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'your_email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your_email_password'
    EMAIL_USE_TLS = True
```
- Edits in *app_name/views.py*:
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
- Edits in *app_name/urls.py*:
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
        # Code to execute after the model instance saved
```
- `my_handler` function is called each time the `post_save` condition is met, such as when a new model instance is created.

## 12. Using Django ORM (Raw SQL in Django):
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

## 13. Payment Gateways in Django (Using RazorPay):
- For Paytm Integration: https://youtu.be/cdtPcTIuazI
- For Razorpay Integration: https://youtu.be/WY1gDoU8xvI

- Install: `pipenv install razorpay`
- Edits in *project_name/settings.py*:
```python
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET') 
```

- Edits in *app_name/models.py*:
```python
from django.db import models

class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, default='Pending')
    razorpay_order_id = models.CharField(max_length=255)
    razorpay_payment_id = models.CharField(max_length=255, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment by {self.user.username} for ₹{self.amount}'
```

- Edits in *app_name/views.py*: 
```python
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
from .models import Payment

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def payment_page(request):
    return render(request, 'payment_page.html')

def create_order(request):
    if request.method == 'POST':
        amount = 5000  # Can be fetched from DB according to item purchased
        currency = 'INR'

        try:
            # Create a Razorpay order
            order = client.order.create(dict(amount=amount, currency=currency, payment_capture='1'))

            # Save Razorpay order_ID to db
            payment = Payment(user=request.user, amount=amount / 100, status='Pending', razorpay_order_id=order['id'])
            payment.save()

            return JsonResponse({
                'razorpay_order_id': order['id'],
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            })
        except razorpay.errors.RazorpayError as e:
            return JsonResponse({'error': str(e)})

    return redirect('payment:payment_page')


@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        # Get payment data from ui
        data = json.loads(request.body)
        razorpay_order_id = data.get('razorpay_order_id')
        razorpay_payment_id = data.get('razorpay_payment_id')
        razorpay_signature = data.get('razorpay_signature')

        # Fetch order object from Razorpay
        try:
            order = client.order.fetch(razorpay_order_id)
        except razorpay.errors.RazorpayError as e:
            return JsonResponse({'success': False, 'error': 'Error fetching Razorpay order'})

        # Verify payment signature
        generated_signature = f"{razorpay_order_id}|{razorpay_payment_id}"
        expected_signature = hashlib.sha256(generated_signature.encode('utf-8')).hexdigest()

        if razorpay_signature == expected_signature: # Payment success, updating the database
            try:
                payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)
                payment.status = 'Completed'
                payment.razorpay_payment_id = razorpay_payment_id
                payment.razorpay_signature = razorpay_signature
                payment.save()

                return JsonResponse({'success': True})

            except Payment.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Payment record not found'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid signature'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})
```

# Extras (New_Apps Config)
## 1. Debug Toolbar
- Install: `pipenv install django-debug-toolbar`
- Edits in *project_name/settings.py*:
```python
INSTALLED_APPS: 'debug_toolbar',
MIDDLEWARE: 'debug_toolbar.middleware.DebugToolbarMiddleware',
TEMPLATES: 'debug_toolbar.context_processors.debug',
INTERNAL_IPS: ['127.0.0.1']
```

## 2. TinyMCE
- Install: `pipenv install tinymce`
- Edits in *project_name/settings.py*:
```python
INSTALLED_APPS: 'tinymce',
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
```