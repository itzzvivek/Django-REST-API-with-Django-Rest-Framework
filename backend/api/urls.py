from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.api_home, name='home'),
    #path('products/', include('products.urls')),
]