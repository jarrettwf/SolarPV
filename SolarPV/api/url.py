from django.urls import path
from . import views
app_name = 'backend'
urlpatterns = [
	path('products/', views.productListView.as_view(), name='product_list'),
	path('products/<pk>/', views.productDetailView.as_view(), name='product_detail'),

	path('certificates/', views.certificateListView.as_view(), name='certificate_list'),
	path('certificates/<pk>/', views.certificateDetailView.as_view(), name='certificate_detail'),

	path('service/', views.serviceListView.as_view(), name='service_list'),
	path('service/<pk>/', views.serviceDetailView.as_view(), name='service_detail'),

]