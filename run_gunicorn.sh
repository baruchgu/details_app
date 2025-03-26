gunicorn -c gunicorn_conf.py src.details.app:app > /dev/null   2>&1
#gunicorn src.details.app:app
