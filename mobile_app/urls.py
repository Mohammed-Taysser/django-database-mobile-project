from django.urls import path
from . import views

app_name = 'mobile_app'

urlpatterns = [
	path('', views.home, name='home'),
	path('customer', views.customer, name='customer'),
	path('department', views.department, name='department'),
	path('employee', views.employee, name='employee'),
	path('order', views.order, name='order'),
	path('product', views.product, name='product'),
	path('discount', views.discount, name='discount'),
	path('supplier', views.supplier, name='supplier'),
	path('customer-details/<slug:customer_ssn>', views.customer_details, name='customer-details'),
	path('employee-details/<slug:employee_ssn>', views.employee_details, name='employee-details'),
	path('department-location', views.department_location, name='department_location'),
	path('department-details/<int:department_number>', views.department_details, name='department-details'),
	path('order-details/<slug:order_num>', views.order_details, name='order-details'),
	path('product-details/<slug:product_num>', views.product_details, name='product-details'),
	path('supplier-details/<slug:supplier_num>', views.supplier_details, name='supplier-details'),
]
