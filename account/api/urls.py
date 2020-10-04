from django.urls import path
from account.api.views import api_user_view, api_user_detail_view

app_name = 'account'

urlpatterns = [
    path('', api_user_view, name='account'),
    path('<int:id>', api_user_detail_view, name="account_detail"),
]