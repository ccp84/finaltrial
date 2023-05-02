# finaltrial

## Steps taken to run this project

-   `pip install 'django<4' gunicorn`
-   `django-admin startproject dryrun .`
-   `python manage.py startapp announcements`
-   Add app to settings

-   Include the URL patterns for app in main project URLS

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('announcements.urls', namespace='annoucements')),
]
```

-   Create URL file in app
-   Create templates / annoucements folder include index.html as blank file

-   Set templates directory in settings `'DIRS': [BASE_DIR / 'templates/'],`

## Models

-   Create models
-   Migrate

## Install REST

-   `pip install djangorestframework`
-   Add `rest_framework` to installed apps

## Create views

## Create Serializers

## Set permissions

-   In settings

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny', //Anyone can access
        'rest_framework.permissions.IsAuthenticated', //Logged in only can access the API
    ]
}
```

## Install Coverage

-   `pip install coverage`
-   `coverage run manage.py test`
-   `coverage html` - open htmlcov in browser
-   Write tests

## Deploy to heroku

`pip3 install dj_database_url==0.5.0 psycopg2`

-   Setup static link to AWS
    `pip install Pillow django-storages boto3` - add storages to installed apps
-   Add elephant database
-   Create env
-   Create procfile
-   Add media, static and templates folders at root level
-   Add allowed hosts to settings
-   migrate
-   install django cors headers `pip install django-cors-headers` add `corsheaders` to installed apps
-   Add middleware above common middleware in settings `'corsheaders.middleware.CorsMiddleware',`
-   Add cors allowed origins

```python
# Under middleware

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]
CORS_ALLOW_CREDENTIALS = True
```

-   freeze to requirements
-   Create heroku app
-   Add config vars
-   Commit and push
-   Deploy to heroku

## Create Custom User Model

-   Create users app
-   Add to installed apps
-   Build model
-   Register model in settings `AUTH_USER_MODEL = 'users.CustomUser'`
-   Use `from django.conf import settings` as import and `settings.AUTH_USER_MODEL` instead of USER for model
-   Migrate

## Active JWT Authentication

[Instructions here](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
Add in token blacklisting for logouts on refresh

## Install allauth

[instructions here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
`pip install dj-rest-auth`
