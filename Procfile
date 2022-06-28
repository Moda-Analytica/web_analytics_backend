web: gunicorn -w 3 -k uvicorn.workers.UvicornWorker app.main:app

celery -A app.push_notification.celery_worker.app worker -l INFO