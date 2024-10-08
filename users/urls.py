from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserListAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update_user'),
    path('', UserListAPIView.as_view(), name='list_user'),
    path('payments/', PaymentListAPIView.as_view(), name='list_payment')
]
