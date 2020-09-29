release: python manage.py migrates
web: gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker

