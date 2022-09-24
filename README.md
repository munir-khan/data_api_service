# Pre-Requisites
Ensure that you have the following installed on the system:
```
python-3.9.x
django-4.1.x
postgreSQL-12.x
```

## Code Repository
Clone repository that contain the updated code in the targeted branch
```
git clone <main-repo> .
```

**`main-repo`** is the URL to clone the main repository from.  
**`main`** is the URL to clone the main repository from.

## Overview

The `DataApiService` project has a `shared_document_store` app primarily 
responsible for storing the digital documents in the system; For this purpose
we will not be storing the actual files in the system but their reference paths.

The system has the following entities that it revolves around;
```
* Folder
* Document
* Topic
```

### Folder

A folder is the actual path of the document file, it denotes the directory path
that the document is stored in. For instance, ``documents/folderName/file.ext``

### Document

A document is the actual file that is saved, in our case ``file.ext``

### Topic

A topic is an entity associated to a document, for instance ``topic_1`` is
associated to document ``file.ext``

## System Flow

A user could add topics and then a folder that'd be followed by a document 
with its association with a topic.

When fetching the documents, the user is expected to provide a folder name and
a topic, the system will search for all the documents in that folder that are
associated with the provided topic.

## Data Modelling

Under the time constraint circumstances, I have chosen to go with the simplest
decent approach of data modelling (link and screenshot attached in the email). 
Further optimum solutions can be discussed, given the opportunity.

## Project Setup

Create a virtual environment under the project root directory

``` python3 -m venv venv```

Activate the virtual environment and install the requirements file.

``` source venv/bin/actiavte ```

``` pip3 install -r requirements.txt ```

#### Run the migration files:

``` python manage.py makemigrations ```

``` python manage.py migrate ```

#### To run the project locally:

``` python3 manage.py runserver 0.0.0.0:8080```

To access the admin site, create a superuser:

``` python3 manage.py createsuperuser ```

# Deployment

The project is currently deployed to heroku, with the following changes in
`settings.py`:

``` import django_heroku ``` at the top of the file

``` # ALLOWED_HOSTS = ['data-api-service.herokuapp.com'] ```

or for the purpose of this exercise

``` # ALLOWED_HOSTS = ['*'] ```

Activate Django-Heroku

``` django_heroku.settings(locals()) ```

`Procfile` in the project root directory that specifies the commands that 
are executed by the app on startup. where we specify a process type by 
adding the below line in the file:

``` web: gunicorn <projectname>.wsgi --log-file - ```

`runtime.txt` in project root directory. This tells Heroku what version of 
python we are using.

To run migrations in heroku:

``` heroku run python manage.py migrate -a <app-name> ```

## Tests
