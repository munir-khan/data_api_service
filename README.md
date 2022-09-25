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

A user should add topics and then a folder that'd be followed by adding a
document with its association with a topic.

1. Add a Topic

`curl --location --request POST 'http://data-api-service.herokuapp.com/topic/' \
--form 'name="topic_2"' \
--form 'description="t2 desc"'`
 
2. Add a Folder

`curl --location --request POST 'http://data-api-service.herokuapp.com/folder/' \
--form 'path="f1/f2/f3/"' \
--form 'name="folder_name"'`

3. Add a Document

`curl --location --request POST 'http://data-api-service.herokuapp.com/document/' \
--form 'name="doc_1"' \
--form 'folder_path="5"' \
--form 'topic_name="1"'`

When fetching the documents, the user is expected to provide a folder name and
a topic, the system will search for all the documents in that folder that are
associated with the provided topic.

1. GET documents in a folder associated to a topic by single call

`curl --location --request GET 'http://0.0.0.0:8080/folder/?topic=topic_1&folder=5'`

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

### Setup Environment variables

```
DB_NAME= <db-name>
DB_USER = <db-user>
DB_PASSWORD = <db-password>
DB_HOST = <db-host>
DB_PORT = <port>
```

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

To access db in heroku:

``` heroku pg:psql -a <app-name> ```

## Tests

The project uses unit tests, to start:

`` python manage.py test``

## Enhancements

The project was time-constraint and hence the room for enhancement is
there, Given the time I had rectified and focused more on the following:

* Better DB Schema

``` Segregating and normalizing more fields ```
* Test Cases

``` Further test cases to cover edge cases ```

* Linters

``` Use of linters like black, flake8 ensuring PEP-8 standards and removing unused imports along with spacings ```

* Type Hinting & doc str

``` Using type hinting and proper doc strings ```

* CI/CD

``` Implementing auto deployments for heroku ```