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