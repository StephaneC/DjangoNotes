# install framework
pip install django djangorestframework coreapi

# Create Django project
django-admin.py startproject DjangoNotes

# Add modules
python manage.py startapp users
python manage.py startapp notes

# dependencies
pip install django
pip install djangorestframework
pip install django-redis

# Run 
python manage.py runserver

# before commit:
find . -name "*.pyc" -type f -delete
