
# 🍋 Little Lemon Restaurant API

This Django REST Framework project provides a backend system for a fictional restaurant, **Little Lemon**. It includes APIs for managing the menu, booking tables, and handling user authentication.

---

## 📁 Project Structure

- `restaurant/` – Main Django app containing models, views, serializers, and API logic.
- `little_lemon/` – Project configuration (settings, URLs, WSGI).
- `tests/` – Contains unit tests for models and views.

---

## 🚀 Features

- **Menu API** – Add, update, list, and delete menu items.
- **Booking API** – Book tables, view and manage bookings.
- **User Registration & Authentication** – Register new users and use token-based authentication.
- **Admin Panel** – Manage models via Django admin interface.

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/UlrikeDetective/LittleLemonBackEnd
cd little_lemon
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure the database**

Make sure you have a MySQL server running. In `settings.py`, update:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon02',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Apply migrations and create superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

---

## 🔐 Authentication

Token-based authentication is implemented using [Djoser](https://djoser.readthedocs.io/en/latest/).

### Key Endpoints

| Method | Endpoint                 | Description                        |
|--------|--------------------------|------------------------------------|
| POST   | `/auth/token/login/`     | Login and obtain auth token        |
| POST   | `/auth/token/logout/`    | Logout user                        |
| POST   | `/auth/users/`           | Register a new user                |

---

## 📡 API Endpoints

| Method        | Endpoint                      | Description                          |
|---------------|-------------------------------|--------------------------------------|
| GET/POST      | `/api/menu/`                  | List or create menu items            |
| GET/PUT/DELETE| `/api/menu/<id>/`             | Retrieve, update or delete item      |
| GET/POST      | `/api/booking/tables/`        | List or create bookings              |
| GET/PUT/DELETE| `/api/booking/tables/<id>/`   | Manage specific booking              |

---

## 🧪 Running Tests

To run unit tests for models and views:

```bash
python manage.py test
```

Test coverage includes:
- Menu model string representation
- Menu API view responses

---

## 🧰 Tools & Libraries Used

- Python & Django
- Django REST Framework
- MySQL
- Djoser
- Insomnia/Postman (for API testing)
- unittest (for backend testing)

---

## 🔍 Example API Paths for Testing

These paths can be used to test API functionality:

```
/api/menu/
/api/menu/<id>/
/api/booking/tables/
/api/booking/tables/<id>/
/auth/users/
/auth/token/login/
/auth/token/logout/
```

---

## 📝 License

This project is for educational purposes and demonstration only. No commercial use intended.
