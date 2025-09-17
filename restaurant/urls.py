from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("items/",views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
]