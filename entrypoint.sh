#1/bin/bash

# Apply database migrations
python manage.py migrate

# Start Celery beat
celery -A CORE beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &

python manage.py populate_db

exec python manage.py runserver 0.0.0.0:8000
