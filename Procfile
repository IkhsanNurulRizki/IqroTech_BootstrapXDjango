web: gunicorn --pythonpath django_project iqrotech_site.wsgi:application
python manage.py collectstatic --noinput
manage.py migrate
