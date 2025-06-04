from . import views
from django.urls import path

urlpatterns = [
    path('', views.PubList.as_view(), name='Pubs'),
    path('<slug:slug>/', views.pub_detail, name='pub_detail'),
]