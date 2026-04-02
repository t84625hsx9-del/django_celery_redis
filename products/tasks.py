from celery import shared_task
import time

@shared_task
def log_new_product(product_name):
    # Имитируем "тяжелую" работу (например, отправку уведомления или обработку фото)
    time.sleep(2) 
    
    print(f"--- [CELERY SUCCESS] ---")
    print(f"Товар '{product_name}' успешно залогирован в фоновом режиме.")
    
    return f"Product {product_name} processed."