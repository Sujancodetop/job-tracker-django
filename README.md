# Job Tracker Django
A Django web application to manage and track job applications. It allows users to add, edit, and view job applications with a simple and fancy design.
## Features
- Add new job applications.
- Edit existing job applications.
- View all job applications.
- Simple user interface with a fancy design using Bootstrap.
## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/sujancodetop/job-tracker-django.git
cd job-tracker-django
python -m venv venv
.\venv\Scripts\activate or source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
## Usage
- **Home Page**: Displays a list of all job applications.
- **Add Job**: Allows you to add new job applications.
- **Edit Job**: Lets you edit existing job applications.
- **Admin Panel**: Accessible at `http://127.0.0.1:8000/admin/` to manage job applications.
## Technologies Used
- Django (Python Framework)
- HTML, CSS, Bootstrap (Frontend styling)
- SQLite (Database)
- ## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



