from django.contrib.auth.forms import ReadOnlyPasswordHashWidget
from django.urls import path
from .views import(
  Create_Account,
  Account_login,
)
from django.contrib.auth import logout

urlpatterns = [
    path('create/', Create_Account, name='create_account'),
    path('login/', Account_login, name='login'),
    path('^logout/', logout, {'template_name': 'index.html'}, name='logout'),
]