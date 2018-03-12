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

# before commit (it no .gitignore):
find . -name "*.pyc" -type f -delete

# WIP
* DO PUT/DELETE/GET for a specific note
* Refactoring of session. SHould be in a specific file in DjangoNote shared between project.
