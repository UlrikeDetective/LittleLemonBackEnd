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