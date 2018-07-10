# 3WM CHALLENGE

Is written in Python with Django framework.

# Clone repo:

```bash
git clone https://github.com/boolow5/3wm-challenge.git

# go to repo home directory
cd 3wm-challenge
```


## To run locally:

To run this app we recommend using python3 and make sure it's installed. This assumes you are running on Unix compatible system.
For Windows you need to tweak the commands.

## 1. Setup virtual environment:

### To create virtual environment run:
```bash
virtualenv -p `which python3` venv
```

### To activate virtual environment run:
```bash
source venv/bin/activate
```

### To get out of the evironment run:
```bash
deactivate
```

## 2. Install requirements:

```bash
pip install -r requirements.txt
```

## 3. Go to app directory:

```bash
cd sitesproject
```

## 4. Prepare the app:

```bash
    # preprate the database
    python manage.py makemigrations
    python manage.py migrate

    # create admin user and password run the below command
    # and then follow the instructions to complete
    python manage.py createsuperuser
```

## 5. Run local server

```bash
python manage.py runserver
```

## 6. Browser
- open http://localhost:8000 on your browser to see the app
- open http://localhost:8000/admin to add sites and items

## 7. Don't have time for adding items and sites?

Load this data using this command:

```bash 
python manage.py loaddata sites.json
```
