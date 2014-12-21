ndia-django
===========

Northside Digital Innovation Alliance (NDIA) project prototype in Django

The Django portion of the NDIA project aims to build a backend to manage and
provide information about public technology centers, classes, and events in
North Minneapolis. The backend will include an API endpoint that enables API
clients to query the above information. The backend will also provide a UI for
administrators to edit and manage the above information.

[ndia-angular](https://github.com/OpenTwinCities/ndia-angular) is intended to
be a client of this backend.

# Dependencies

##Python

Make sure you have Python on your computer. The following two commands should work:

```
python --version
pip --version
```
## Recommended - virtualenv and virtualenvwrapper

[Virtualenv](https://virtualenv.readthedocs.org/en/latest/) makes it possible 
to install multiple Python environments on one computer; including installing a 
Python environment just for this project. It is not required to run this, but
if you're working on multiple Python projects, you should probably install this.

[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) 
provides commands and organization for using multiple virtualenvs.

Instructions in this README assume that virtualenv and virtualenvwrapper are
installed and make use of those tools.

### Install

```
pip install virtualenv
pip install virtualenvwrapper
```

# Get Northside Digital Assets System

```
git clone https://github.com/OpenTwinCities/ndia-django.git
cd ndia-django
mkvirtualenv ndia-djagno
```

# Update and Run Northside Digital Assets System

```
cd ndia-django
git pull
workon ndia-django
pip install -r requirements.txt
python manage.py runserver
```
