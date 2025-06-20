# 🍋 Little Lemon Backend

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

The backend service for Little Lemon Restaurant, developed as part of the Meta Back-End Developer Professional Certificate program. This Django-based REST API provides a robust foundation for managing restaurant operations.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- MySQL Server

### ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/LittleLemonBackEnd.git
   cd LittleLemonBackEnd
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 🛠️ Configuration

1. **Create Django project** (skip if already done)
   ```bash
   django-admin startproject little_lemon
   ```

2. **Database Setup**
   - Configure your MySQL database settings in `little_lemon/settings.py`
   - Change the current directory to littlelemon and create a djangoapp with the name restaurant.
     ```bash
     python manage.py migrate
     ```

3. **Create Django app**
```bash
   python manage.py startapp restaurant
   ```
### 🔥 Running the Server
1. **Start development server**
   ```bash
   cd little_lemon
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`

## 📝 API Documentation

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/menu/` | GET | Retrieve menu items |
| `/api/booking/` | POST | Create a booking |

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Exercise: Setting up the Django project
Overview
In this Capstone project course, you are going to build REST APIs using Django and Django REST Framework.

In this exercise, you will build a Django project for the Little Lemon restaurant.

Scenario
The owners of the Little Lemon restaurant have hired you to build two APIs. One API to order food using the Menu API. You need to build the Table booking API to facilitate reserving a table for dining in the restaurant on a specific date and for a certain number of people.

Scenario
For the capstone project, you will build a REST API for ordering food and table reservation.

Step 1: Create a templates directory

The project package folder and the app package folder both are created inside the outer folder which is identified as BASE_DIR. Inside this BASE_DIR  create a template directory/folder named templates.

Step 2: Include the templates directory in settings.py

In VS Code, go to the TEMPLATES section in the settings.py file and ensure that the templates directory created in the above step is in the list of the DIRS attribute.

#Include 'templates' in 'DIRS' attribute
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Step 3: Create index.html

Inside the templates folder, create a new file called index.html and put the following script in it.

<html>
   <head>
      <title>Capstone Project</title>
   </head>
   <body>
      <h1 style="text-align:center;">Welcome ToLittleLemon Restaurant</h1>
   </body>
</html>

Step 4: Define index view

Open the views.py file from the restaurant folder. Add the following function:

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

Step 5: Add the URL route

Open the urls.py file from the restaurant folder. Make sure that the following path is added to the urlpatterns list.

#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    . . . ,
    path('', views.index, name='index')
]

Step 6: Update URLConf

Open the urls.py file from the Littlelemon folder. Include the URL patterns of the restaurant app in it.

#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path(restaurant/', include(restaurant.urls'))
]

Step 7: Visit the home page

Run the Django server with the manage.py script and visit the http://localhost:8000/restaurant/ URL.

Step 8: Save the LittleLemon.png image

All the static assets must be placed in the restaurant/static/restaurant folder. Put the littlelemon.png file here.

Step 9: add the static tag in index.html

Modify the index.html file to include the following statements.

<!--add this template tag-->
{% load static %}
<img src="{% static 'restaurant/littlelemon.png' %}">

Step 10: Refresh the home page

You should see the image rendered on the browser.

MySQL Database Setup
1. **Install MySQL Server**: Follow the installation instructions for your operating system.
2. mysql -u root -p
3. **Install MySQL client for Python**: Ensure you have the MySQL client installed in your virtual environment:
   ```bash
   pip install mysqlclient
   ```
4. **Create a database**: Open your MySQL client and run the following command:
   ```sql
   CREATE DATABASE little_lemon;
   ```
5. **Create a user**: Create a new user and grant privileges to the database:
   ```sql
   CREATE USER 'little_lemon_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON little_lemon.* TO 'little_lemon_user'@'localhost';
   FLUSH PRIVILEGES;
   ```      
6. **Update settings.py**: Modify your Django project's `settings.py` file to connect to the MySQL database:
   ```python
   #Settings.py 
 DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'LittleLemon',   
        'USER': 'root',   
        'PASSWORD': '',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',   
        'OPTIONS': {   
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
        }   
    }   
}

exit mysql client by typing `exit;`

7. **Migrate the database**: Run the following command to create the necessary tables in your MySQL database:
   ```bash
   python manage.py migrate
   ```
   Step 6

Note that the MySQL tab appears in the file explorer bar of VS Code
Click on +  button and connect to the database. Enter localhost as the domain name and null password when prompted.


Now localhost appears in the MySQL tab.
8. **Create a superuser**: Create a superuser to access the Django admin interface:
   ```bash
   python manage.py createsuperuser
   ```
9. **Run the server**: Start the Django development server:
   ```bash
   python manage.py runserver
   ```
Step 7

Expand the localhost to find your database – LittleLemon. Double click it to show the tables created by the migrate command

✅ Step-by-Step Actions in VS Code
✅ 1. Open your project in VS Code
Project folder should be named: LittleLemon

Inside it, you should see an app folder: restaurant

✅ 2. Define the Models
Open restaurant/models.py and paste this code:

python
Copy
Edit
from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
✅ 3. Connect Django to MySQL
Open LittleLemon/settings.py and update the DATABASES section:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',           # Your DB name
        'USER': 'root',                  # Or your MySQL username
        'PASSWORD': 'yourpassword',      # Replace with your password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
🔁 If you're using PyMySQL, also open LittleLemon/__init__.py and add:

python
Copy
Edit
import pymysql
pymysql.install_as_MySQLdb()
✅ 4. Run the Migrations
Open the terminal in VS Code:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
You should see confirmation that tables were created.

✅ 5. Register the Models in Admin
Open restaurant/admin.py and add:

python
Copy
Edit
from django.contrib import admin
from .models import Menu, Booking

admin.site.register(Menu)
admin.site.register(Booking)
✅ 6. Create a Superuser
In the terminal:

bash
Copy
Edit
python manage.py createsuperuser
Set a username, email, and password.

✅ 7. Start the Development Server
bash
Copy
Edit
python manage.py runserver
Open http://127.0.0.1:8000/admin

Log in using your superuser credentials.

✅ 8. Add Data via the Admin Interface
Add Menu items (e.g., Burger, Salad, etc.)

Add Booking entries (e.g., Alice, 3 guests, 2025-06-21 18:00)

✅ 9. Verify Data in MySQL
In your MySQL browser extension in VS Code:

Refresh the database

View the restaurant_menu and restaurant_booking tables

You should see the new entries

Username (leave blank to use 'ulrike_imac_air'): littlelemon01
Email address: littlelemon01@lemons.com
Password: lemons01
Password (again): 

Exercise: Set up the menu API
Overview
In previous exercises, you have already set up a LittleLemon project that includes the Restaurant app. You have also declared the Menu and Booking models, migrated to the MySQL database.

In this exercise, you will build a REST API to perform CREATE, READ, UPDATE AND DELETE operations on the Menu model

Scenario
You will use Django REST Framework to build the APIs in the restaurant app. You will also create the views using DRF's generic views.

Step 1

Install the 'rest_framework' with pip install djangorestframework utility while remaining in the Django virtual environment directory.

Open the command prompt in the LittleLemon directory and start VS Code.

Step 2

Open the settings.py file and add 'rest_framework' in the LittleLemon project's INSTALLED_APPS list.

Step 2

Open the settings.py file and add 'rest_framework' in the LittleLemon project's INSTALLED_APPS list.

Step 3

The Serializer in Django REST Framework converts compound data types into JSON or XML format. ModelSerializer is a special type of serializer that quickly creates a serializer class from the Django model fields.

The ModelSerializer class is declared in the rest_framework.serializers module.

In the app package folder, create a new file called serializers.py and declare the MenuSerializer class that subclasses ModelSerializer.

Step 4

Open the views.py module in the restaurant app package folder. 

Declare two classes:

MenuItemView – inheriting the rest_framework.generics.ListCreateView class. It handles the POST and GET method calls.

SingleMenuItemView – inherits the RetrieveUpdateAPIView and DestroyAPIView classes both imported from the rest_framework.generics module. This class is responsible for processing GET, PUT and DELETE method calls.

Step 5

Define URL routes for the restaurant app's menu views in the urls.py file.

123
#add following lines to urlpatterns list 
path('menu/', views.MenuItemsView.as_view()),
path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
Include app URLs in the LittleLemon project's urls.py module.

12
#add following line to urlpatterns list 
path('restaurant/menu/',include(restaurant.urls'))  
Step 6

Run Django server, and open the URL http://localhost:8000/restaurant/menu/items. 

This is the URL of the browsable API. Perform POST operations to add menu items. With the GET request, fetch the list of items.

Tips

Use the following code snippet to declare the serializer class:

123456789
#define Serializer class for User model
from django.contrib.auth.models import User 
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = User 
        fields = ['url', 'username', 'email', 'groups']
You can use the following code snippet to define views:

123456789101112
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView): 
queryset = MenuItem.objects.all() 
serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):     



