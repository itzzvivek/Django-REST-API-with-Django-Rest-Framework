from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns=[
    path('auth/',obtain_auth_token),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(),name='token_verify'),
    path('', views.api_home, name='home'),
    #path('products/', include('products.urls')),
]