from products.views import ProductListView, ProductCreateView,ProductDeleteView,ProductDetailView,ProductUpdateView
from django.urls import path

urlpatterns=[
    path('',ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]