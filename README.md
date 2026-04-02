### 1. Клонируйте репозиторий
```bash
git clone https://github.com
cd django_celery_radis
``` 

### 2. Установите зависимости
```bash
pip3 install django celery redis
``` 

### 3. Запустите Redis
```bash
docker run -d -p 6379:6379 redis
``` 

### 4. Запустите Celery Worker
```bash
python3 -m celery -A myproject worker --loglevel=info
``` 

### 5. Протестируйте задачу (создайте ещё одно окно терминала) 
```bash
python3 manage.py shell
from products.tasks import log_new_product
log_new_product.delay("MacBook Pro M3")
``` 