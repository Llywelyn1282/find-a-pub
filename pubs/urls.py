from . import views
from django.urls import path

urlpatterns = [
    path('', views.PubList.as_view(), name='Pubs'),
]