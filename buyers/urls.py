from django.urls import path 
from . import views 

urlpatterns = [
    path('register/', views.BuyerRegistrationView.as_view(), name='buyer_registration'),
    path('enroll-product/', views.BuyerEnrollProductView.as_view(), name='buyer_enroll_product'),
    path('products/', views.BuyerProductListView.as_view(), name='buyer_product_list'),
    path('product/<pk>/', views.BuyerProductDetailView.as_view(), name='buyer_product_detail'),
    path('product/<pk>/<subcategory_id>/', views.BuyerProductDetailView.as_view(), name='buyer_product_detail_subcategory'),

]
