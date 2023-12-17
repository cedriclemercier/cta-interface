# CTA Dashboard

## Manual Build 


> 👉 Install modules via `VENV`  

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For WINDOWS:

```bash
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 
