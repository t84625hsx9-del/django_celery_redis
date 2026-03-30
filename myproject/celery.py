import os
from celery import Celery

# 1. Указываем переменную окружения с настройками Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 2. Создаем экземпляр приложения Celery
app = Celery('myproject')

# 3. Загружаем настройки из settings.py (все, что начинаются с CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# 4. Автоматически ищем файлы tasks.py во всех установленных приложениях (INSTALLED_APPS)
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')