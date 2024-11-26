from django.urls import path
from . import views
from django.urls import path, include

from .views import health_check

from .views import favicon

urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('complete/<int:item_id>/', views.complete_item, name='complete_item'),
    path('health', health_check, name='health_check'),
    path('favicon.ico', favicon, name='favicon'),
]