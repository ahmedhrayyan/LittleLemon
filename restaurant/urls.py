from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'menu/', views.MenuItemView.as_view()),
    path(r'menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path(r'api-token-auth/', obtain_auth_token),
]
