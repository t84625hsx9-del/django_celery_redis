from celery import shared_task

@shared_task
def log_new_product(product_name):
    # Эта логика выполнится в отдельном процессе Celery
    print(f"--- [CELERY] В систему добавлен товар: {product_name} ---")
    return f"Товар '{product_name}' успешно залогирован."