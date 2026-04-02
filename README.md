# Django + Celery + Redis

Проект для выполнения фоновых задач по логированию товаров.

### 1. Установите зависимости
```bash
pip3 install django celery redis
```

### 2. Запустите Redis
```bash
docker run -d -p 6379:6379 redis
```

### 3. Запустите Celery Worker
```bash
python3 -m celery -A myproject worker --loglevel=info
```

### 4. Запустите сервер Django (в новом окне терминала)
```bash
python3 manage.py runserver
```

### Протестируйте задачу (в новом окне терминала)
```bash
python3 manage.py shell
from products.tasks import log_new_product
log_new_product.delay("Bread")
```

