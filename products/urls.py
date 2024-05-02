from django.urls import path
from products import views
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='productList'),
    path('products/<int:pk>/', views.ProductDetailedView.as_view(), name='productDetailed'),
    path('products/create/', views.ProductCreateView.as_view(), name='productCreate'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='productUpdate'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='productDelete'),
    path('categories/', views.CategoryListView.as_view(), name='categoryList'),
    path('categories/<int:pk>/', views.CategoryDetailedView.as_view(), name='categoryDetailed'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='categoryCreate'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='categoryUpdate'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='categoryDelete'),
]