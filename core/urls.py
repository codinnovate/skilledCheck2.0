from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.initiate_payment, name="initiate-payment"),
    # path('<str:ref>/', viewsold.verify_payment, name="verify-payment"),
    path('paystack/callback/', views.paystack_callback, name='paystack_callback'),

]