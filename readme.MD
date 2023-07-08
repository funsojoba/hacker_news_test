# HackerNews 🔖

---

This is a Django implementation of the famous HackerNews API, with a write and update feature for logged in users to add their own news

## Technologies used
* Framework -> `Django`
* Task queue -> `Celery`
* Message broker -> `Redis`
* Database -> `sqlite3`

## To get started
### If you will be using docker, please run the following commands
* `make build`
* `make up`
the code will run on `127.0.0.1:8000`

### else
in the code directory, create and activate the virtual environment
* `python3 -m venv venv && source venv/bin/activate`
* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py populate_db`
and lastly, run
* `python manage.py runserver`

The app will run on `127.0.0.1:8000` and if you chose to use a different port, you can run `python manage.py runserver <port>` and visit `127.0.0.1:<port>` where `<port>` is a variable for your specified port


Happy hacking 👍