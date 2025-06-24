from . import views
from django.urls import path

urlpatterns = [
    path('', views.PubList.as_view(), name='Pubs'),
    path('filter/', views.pub_filtered_list, name='pub_filtered_list'),
    path('<slug:slug>/', views.pub_detail, name='pub_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
