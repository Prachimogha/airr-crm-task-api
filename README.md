# Airr CRM Task API

A Django REST framework project for managing tasks with JWT authentication.

## Installation
```bash
git clone https://github.com/Prachimogha/airr-crm-task-api.git
cd airr-crm-task-api
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver