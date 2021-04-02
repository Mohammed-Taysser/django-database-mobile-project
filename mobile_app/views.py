from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models

# Create your views here.


def home(request):
	data = {
		'page_name': 'home'.title(),
	}
	return render(request, 'mobile_app/home.html', data)


def customer(request):
	db_customer_objects = models.Customer.objects.all()
	paginator = Paginator(db_customer_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_customer_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_customer_objects = paginator.page(1)
	except EmptyPage:
		db_customer_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'customer'.title(),
		'page': current_page,
		'db_customer_objects': db_customer_objects,
	}
	return render(request, 'mobile_app/customer.html', data)


def department(request):
	db_department_objects = models.Department.objects.all()
	paginator = Paginator(db_department_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_department_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_department_objects = paginator.page(1)
	except EmptyPage:
		db_department_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'department'.title(),
		'page': current_page,
		'db_department_objects': db_department_objects,
	}
	return render(request, 'mobile_app/department.html', data)


def department_location(request):
	db_department_objects = models.DepartmentLocation.objects.all()
	paginator = Paginator(db_department_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_department_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_department_objects = paginator.page(1)
	except EmptyPage:
		db_department_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'department'.title(),
		'page': current_page,
		'db_department_objects': db_department_objects,
	}
	return render(request, 'mobile_app/department_location.html', data)


def customer_details(request, customer_ssn):
	current_customer = get_object_or_404(models.Customer, pk=customer_ssn)
	db_discount_objects = models.CustomerDiscountBridge.objects.filter(customer_ssn=current_customer.ssn)
	db_order_objects = models.CustomerOrderBridge.objects.filter(customer_ssn=current_customer.ssn)
	paginator = Paginator(db_order_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_order_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_order_objects = paginator.page(1)
	except EmptyPage:
		db_order_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': (current_customer.fname + ' ' + current_customer.lname).title(),
		'current_customer': current_customer,
		'db_discount_objects': db_discount_objects,
		'db_order_objects': db_order_objects,
	}
	return render(request, 'mobile_app/customer_details.html', data)


def employee(request):
	db_employee_objects = models.Employee.objects.all()
	paginator = Paginator(db_employee_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_employee_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_employee_objects = paginator.page(1)
	except EmptyPage:
		db_employee_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'employee'.title(),
		'db_employee_objects': db_employee_objects,
	}
	return render(request, 'mobile_app/employee.html', data)


def employee_details(request, employee_ssn):
	current_employee = get_object_or_404(models.Employee, pk=employee_ssn)
	db_order_objects = models.EmployeeOrderBridge.objects.filter(employee_ssn=current_employee.ssn)
	paginator = Paginator(db_order_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_order_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_order_objects = paginator.page(1)
	except EmptyPage:
		db_order_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': (current_employee.fname + ' ' + current_employee.lname).title(),
		'current_employee': current_employee,
		'db_order_objects': db_order_objects,
	}
	return render(request, 'mobile_app/employee_details.html', data)


def order(request):
	db_order_objects = models.Order.objects.all()
	paginator = Paginator(db_order_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_order_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_order_objects = paginator.page(1)
	except EmptyPage:
		db_order_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'order'.title(),
		'page': current_page,
		'db_order_objects': db_order_objects,
	}
	return render(request, 'mobile_app/order.html', data)


def product(request):
	db_product_objects = models.Product.objects.all()
	paginator = Paginator(db_product_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_product_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_product_objects = paginator.page(1)
	except EmptyPage:
		db_product_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'products'.title(),
		'page': current_page,
		'db_product_objects': db_product_objects,
	}
	return render(request, 'mobile_app/product.html', data)


def supplier(request):
	db_supplier_objects = models.Supplier.objects.all()
	paginator = Paginator(db_supplier_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_supplier_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_supplier_objects = paginator.page(1)
	except EmptyPage:
		db_supplier_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'suppliers'.title(),
		'page': current_page,
		'db_supplier_objects': db_supplier_objects,
	}
	return render(request, 'mobile_app/supplier.html', data)


def discount(request):
	db_discount_objects = models.Discount.objects.all()
	paginator = Paginator(db_discount_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_discount_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_discount_objects = paginator.page(1)
	except EmptyPage:
		db_discount_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'discounts'.title(),
		'page': current_page,
		'db_discount_objects': db_discount_objects,
	}
	return render(request, 'mobile_app/discount.html', data)


def department_details(request, department_number):
	current_department = get_object_or_404(models.Department,pk=department_number)
	db_employee_objects = models.Employee.objects.filter(dno=department_number)
	paginator = Paginator(db_employee_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_employee_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_employee_objects = paginator.page(1)
	except EmptyPage:
		db_employee_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'department details'.title(),
		'page': current_page,
		'db_employee_objects': db_employee_objects,
		'current_department': current_department,
	}
	return render(request, 'mobile_app/department_details.html', data)


def order_details(request, order_num):
	current_order = get_object_or_404(models.Order,pk=order_num)
	db_employee_objects = models.EmployeeOrderBridge.objects.filter(order_number=order_num)
	db_product_objects = models.ProductOrderBridge.objects.filter(order_number=order_num)
	paginator = Paginator(db_employee_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_employee_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_employee_objects = paginator.page(1)
	except EmptyPage:
		db_employee_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'department details'.title(),
		'page': current_page,
		'db_employee_objects': db_employee_objects,
		'current_order': current_order,
		'db_product_objects': db_product_objects,
	}
	return render(request, 'mobile_app/order_details.html', data)


def product_details(request, product_num):
	current_product = get_object_or_404(models.Product,pk=product_num)
	db_supplier_objects = models.SupplierProductBridge.objects.filter(product_number=product_num)
	db_order_objects = models.ProductOrderBridge.objects.filter(product_number=product_num)
	paginator = Paginator(db_order_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_order_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_order_objects = paginator.page(1)
	except EmptyPage:
		db_order_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'product details'.title(),
		'page': current_page,
		'db_order_objects': db_order_objects,
		'current_product': current_product,
		'db_supplier_objects': db_supplier_objects,
	}
	return render(request, 'mobile_app/product_details.html', data)


def supplier_details(request, supplier_num):
	current_supplier = get_object_or_404(models.Supplier,pk=supplier_num)
	db_product_objects = models.SupplierProductBridge.objects.filter(supplier_number=supplier_num)
	db_phone_objects = models.SupplierPhone.objects.filter(supplier_number=supplier_num)
	paginator = Paginator(db_product_objects, 10)
	current_page = request.GET.get('page')
	try:
		db_product_objects = paginator.page(current_page)
	except PageNotAnInteger:
		db_product_objects = paginator.page(1)
	except EmptyPage:
		db_product_objects = paginator.page(paginator.num_pages)
	data = {
		'page_name': 'supplier details'.title(),
		'page': current_page,
		'db_product_objects': db_product_objects,
		'current_supplier': current_supplier,
		'db_phone_objects': db_phone_objects,
	}
	return render(request, 'mobile_app/supplier_details.html', data)
