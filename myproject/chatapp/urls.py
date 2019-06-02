from django.urls import include, path
from .views import _login,signUp

urlpatterns = [
    path('', _login,name='login'),
    path('sign_up',signUp, name='sign-up')
]
