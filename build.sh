#1/bin/bash

celery -A platform_api beat \
  -l INFO \
  --scheduler django_celery_beat.schedulers:DatabaseScheduler  \
  &> /src/logs/celery.log &