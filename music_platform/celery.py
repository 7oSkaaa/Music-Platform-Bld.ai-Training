import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_platform.settings')
app = Celery("music_platform")
app.config_from_object("django.conf:settings", namespace="CELERY_CONF")
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Cairo')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
