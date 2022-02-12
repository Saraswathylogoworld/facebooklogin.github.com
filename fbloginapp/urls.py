from django.urls import path
from . import views

urlpatterns =[
    path('login',views.login,name='login'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('Flogout',views.Flogout,name='Flogout'),
    path('tem',views.tem,name='tem'),
    path('',views.index,name='index'),
    path('wdisplay',views.wdisplay,name='wdisplay')
]