# Vision

A web app created with the Django framework in python as a backend.

## How to contribute

* HTML code should be added under the "templates" directory
* CSS and JavaScript should be added under the "static" directory and subsequently in their respective sub-directory
* Python code should generally be under the "app" directory

## How to test

First you need to install the dependencies for this project by running the following command in a terminal

```bash
pip install -r requirements.txt
```

In order to create the necessary SQL statements you are going to need to run

```bash
python manage.py migrate
```

In order to execute the service localy run the following command in a terminal

```bash
python manage.py runserver
```

If you wish to create an admin account you will need to run

```bash
python manage.py createsuperuser
```

## Credits

* **Original Repo** -> [repo](https://github.com/sswapnil2/django-quiz-app.git)