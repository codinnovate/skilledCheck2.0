from django.db import models
from django.urls import reverse
import secrets
# from .d import PayStack
# Create your models here.

from accounts.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=5500)
    email = models.EmailField()
    reference = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self) -> str:
        return f"{self.user.email} - {self.amount}"

    def save(self, *args, **kwargs):
        while not self.reference:
            reference = secrets.token_urlsafe(50)
            object_with_similar_reference = Payment.objects.filter(reference=reference).first()
            if not object_with_similar_reference:
                self.reference = reference
        super().save(*args, **kwargs)

    def amount_value(self):
        return self.amount * 100

    
    # def verify_payment(self):
    #     paystack = PayStack()
    #     status, result = paystack.verify_payment(self.reference, self.amount)
    #     if status:
    #         self.paystack_response = result
    #         if result["amount"] / 100 == self.amount:
    #             self.completed = True
    #         self.save()
    #         return True
    #     return False
