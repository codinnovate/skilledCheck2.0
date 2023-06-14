from django.urls import path
from .views import *


urlpatterns=[

     path('SignupType/', register, name='register'),
     path('skilled/', user_login, name='login'),
     path('explore/', FreelancerList.as_view(), name='explore'),
     path('explore/<int:pk>/', FreelancerDetail.as_view(), name='singleuser'),
     path('client_register/', client_register.as_view(), name='client_register'),
     path('freelancer_register/', freelancer_register.as_view(), name='freelancer_register'),
     path('payment/', payment, name = 'payment'),
     path('', login_view_freelancer, name='login_freelancer'),
     path('Client/', login_view_freelancer, name='login_client'),
     path('logout/', logout_view, name='logout'),
     # path('client/otp/<uid>/',  otp_client, name='otp'),
     path('otp/<uid>/',  otp_freelancer, name='otp'),
     path('share/', Referothers.as_view(), name='share')

]