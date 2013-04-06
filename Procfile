web: python manage.py collectstatic --noinput; python manage.py syncdb --migrate; gunicorn_django --workers=4 --bind=0.0.0.0:$PORT openspace/settings.py
