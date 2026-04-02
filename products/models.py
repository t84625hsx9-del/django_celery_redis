from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['-created_at']
    
