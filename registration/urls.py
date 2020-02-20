from django.urls import path
from . import  views
urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('<int:request_id>',views.details,name='details'),
]