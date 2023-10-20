from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'menu/', views.MenuItemView.as_view()),
    path(r'menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
