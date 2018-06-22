# django-rest-service

### This project contains example of how to create restfull web service using django framework. 

# Requirements
* PyCharm Editor
* Python 2.7.12
* Django 1.11.13
* Ubuntu 16.04
* MySQL Server 5.7.x

### Check Python installation using below</br>
   $ python -V </br>
   Python 2.7.12

### Install Django</br>
    sudo pip  install Django==1.11</br>
    
### Check Djangoo installation
```
   $python</br>
   >>> import django</br>
   >>> django.get_version()</br>
   '1.11.13'</br>
```

### Install rest_framework</br>
   $ sudo pip install djangorestframework</br>

### Install python mysqlclient 
```
pip install mysqlclient

```

Import project into PyCharm and navigate to settings.py file under django_service folder .
Change database settings as per local configuration</br>
```
     DATABASES = {
             'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'tutorial',
                    'USER': 'root',
                    'PASSWORD': 'root',
                    'HOST': 'localhost',
                    'PORT': 3306,

          }
      }
```

 Now
 
 ```
 cd django-rest-service/
 
 ```
 
 ### update table structure
 ```
python manage.py makemigrations
python manage.py migrate
```
Now check in databse table called services_employees will be created
 ### Create super user, This will be used to login admin dashboard.
 ```
 python manage.py createsuperuser
 
 ```
#runing application server on port 8088
```
python manage.py runserver 0:8088
```
### Verify application 
hit http://localhost:8088/employees/  should be able to see below screen

![Alt text](home_screen.png?raw=true "Title")

