from django.db import models
from accounts.models import User

class Receipt(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    # product = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.quantity} x {self.price}) = {self.total}"
    

Whatsapp_choices = (
    ("Group", "Group"),
    ("Community", "Community"),
    )
Telegram_choices = (
    ("Group", "Group"),
    ("Channel", "Channel"),
)


class Whatsapp(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    Type = models.CharField(max_length=12, choices=Whatsapp_choices)
    title = models.CharField(max_length=200, blank=False)
    link = models.URLField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Whatsapp Platforms'

    
class Telegram(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    Type = models.CharField(max_length=12, choices=Telegram_choices)
    title = models.CharField(max_length=200, blank=False)
    link = models.URLField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Telegram Platforms'

