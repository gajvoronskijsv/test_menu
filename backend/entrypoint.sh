python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

gunicorn 'backend.wsgi' --bind=0.0.0.0:8000

