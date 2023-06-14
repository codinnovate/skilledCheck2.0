from django.urls import path
from .import  views
from accounts.views import FreelancerList, FreelancerDetail
urlpatterns=[
     path('',views.home, name='home'),
     path('dashboard/', views.Dashboard, name='dashboard'),
     path('explore/', FreelancerList.as_view(), name='Freelancers'),
     path('explore/<int:pk>/', FreelancerDetail.as_view(), name='Freelancers'),
     path('Terms', views.privacy, name='privacy'),
     # path('receipt/', views.generate_receipt, name='generate_receipt_pdf'),
]
