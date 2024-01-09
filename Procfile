web: gunicorn -b 127.0.0.1:8001 iqrotech_site.iqrotech_site.wsgi:application
python manage.py collectstatic --noinput
manage.py migrate
