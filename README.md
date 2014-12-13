ndia-django
===========

Northside Digital Innovation Alliance project prototype in Django

# Dependencies

##Python

Make sure you have Python on your computer. The following two commands should work:

```
python --version
pip --version
```
## Recommended - virtualenv

[Virtualenv](https://virtualenv.readthedocs.org/en/latest/) makes it possible 
to install multiple Python environments on one computer; including installing a 
Python environment just for this project. It is not required to run this, but
if you're working on multiple Python projects, you should probably install this.

### Install

```
pip install virtualenv
```

# Get Northside Digital Assets System

```
git clone https://github.com/OpenTwinCities/ndia-django.git
cd ndia-django
virtualenv env
```

# Update and Run Northside Digital Assets System

```
cd ndia-django
git pull
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
