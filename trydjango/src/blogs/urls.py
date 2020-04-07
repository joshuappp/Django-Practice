from django.urls import path
from blogs.views import article_list_view,article_create_view,article_detail_view,article_update_view,article_delete_view

urlpatterns = [

    path('<int:my_id>/detail/',article_detail_view,name='article_detail'),
    path('<int:my_id>/update/',article_update_view,name='article_update'),
    path('list/',article_list_view,name='article_list'),
    path('<int:my_id>/delete/',article_delete_view,name='article_delete'),
    path('create/',article_create_view,name='article_create'),
    
]