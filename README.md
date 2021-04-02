
## REQUIREMENTS
1. [python](https://www.python.org/downloads/)
2. [pip](https://pypi.org/project/pip/) 
3. [postgres](https://www.postgresql.org/)


> install pip in window ``python get-pip.py``
## INSTALLATION
```markdown
1. git clone https://github.com/Mohammed-Taysser/django-database-mobile-project.git
2. cd django-database-mobile-project
3. pip install -r requirements.txt
4. python manage.py runsever

```

## note

 the database name is `django_mobile_project` so use should change the user name and password to your own one

you will find it on `setting.py` in `mobile_project` folder

```markdown
django-database-mobile-project/
    manage.py
    mobile_project/
        __init__.py
        settings.py     <== here
        urls.py
        asgi.py
        wsgi.py
```
```python
....

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_mobile_project',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
.... 
```