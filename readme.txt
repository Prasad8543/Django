1. Creating Virtual Environment
	pip3 install virtualenv
	python3.7 -m venv env_name
2. Activate the virtualenv
	source env_name/bin/activate
3. Django Project 
	django-admin startproject django_project
4. Django App
	django-admin startapp django_app
5. Create a model
6. Register models in admin.py
7. Makemigrations
	python3 manage.py makemigrations
8. Run Migrations
	python3 manage.py migrate
9. Runserver
	python3 manage.py runserver