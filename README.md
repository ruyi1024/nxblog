
a high performance blog system by python django.

# Install

Requrired:
MySQL > 5.1
Python = 2.7

Install Django Packet:
```
# pip install Django==1.9.12
# pip install xadmin
# pip install django-crispy-forms
# pip install django-reversion
# pip install importlib
# pip install markdown2
# pip install django_markdown
# pip install django-markdownx
# pip install django-pagedown
# pip install MySQL-python   (or # yum -y install MySQL-python.x86_64)
```
Clone Nxblog :
```
# git clone https://github.com/ruzuojun/nxblog.git
```
Database Settings:
```
# cd nxblog/
# vim nxblog/settings.py
```
--modify mysql connection follow example :
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nxblog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

Collect Static:
```
# python manage.py collectstatic
```
Migrate DB:
```
# python manage.py migrate
```
Create Super User:
```
# python manage.py createsuperuser
```
Runserver:
```
# python manage.py runserver 
```
Blog URL:
http://127.0.0.1:8000/

Admin URL:
http://127.0.0.1:8000/admin

Xadmin URL:
http://127.0.0.1:8000/xadmin

