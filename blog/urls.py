from django.urls import path
from .views import asosiypage,about,client,contact,index,products

urlpatterns =[
    path('', asosiypage, name ='index'),
    path('about/',about,name = 'about'),
    path('client/',client,name = 'client'),
    path('contact/',contact,name ='contact'),
    path('index/',index,name = 'index'),
    path('products/',products,name='products')

]