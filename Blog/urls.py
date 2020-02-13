from django.urls import path
from .views import (ArticleListView)


app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # path('create', product_create_view, name='product-list'),
    # path('product_list', product_list_view, name='product-list'),
    # #path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),
    # path('<int:id>/', product_detail_view, name='product-detail'),
    # path('<int:id>/delete', product_delete_view, name='product-delete'),
]