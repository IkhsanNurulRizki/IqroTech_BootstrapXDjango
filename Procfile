web: gunicorn --pythonpath radio radio.wsgi
python manage.py collectstatic --noinput
manage.py migrate
