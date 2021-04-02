from django.db import models

# Create your models here.


class Customer(models.Model):
    ssn = models.CharField(primary_key=True, max_length=20)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'customer'
    
    def __str__(self):
        return self.fname + ' ' + self.lname


class CustomerDiscountBridge(models.Model):
    customer_ssn = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_ssn')
    discount_num = models.OneToOneField('Discount', models.DO_NOTHING, db_column='discount_num', primary_key=True)

    class Meta:
        managed = False
        db_table = 'customer_discount_bridge'
        unique_together = (('discount_num', 'customer_ssn'),)


class CustomerOrderBridge(models.Model):
    customer_ssn = models.OneToOneField(Customer, models.DO_NOTHING, db_column='customer_ssn', primary_key=True)
    order_num = models.ForeignKey('Order', models.DO_NOTHING, db_column='order_num')

    class Meta:
        managed = False
        db_table = 'customer_order_bridge'
        unique_together = (('customer_ssn', 'order_num'),)


class Department(models.Model):
    manager_ssn = models.CharField(max_length=20)
    department_name = models.CharField(max_length=50)
    department_num = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'department'
    
    def __str__(self):
        return self.department_name


class DepartmentLocation(models.Model):
    department_num = models.OneToOneField(Department, models.DO_NOTHING, db_column='department_num', primary_key=True)
    department_location = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'department_location'
        unique_together = (('department_num', 'department_location'),)


class Discount(models.Model):
    discount_num = models.IntegerField(primary_key=True)
    discount_value = models.DecimalField(max_digits=10, decimal_places=3)
    end_date = models.DateTimeField()
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'discount'


class Employee(models.Model):
    ssn = models.CharField(primary_key=True, max_length=20)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthdate = models.DateField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    salary = models.IntegerField()
    dno = models.ForeignKey(Department, models.DO_NOTHING, db_column='dno')

    class Meta:
        managed = False
        db_table = 'employee'
        
    def __str__(self):
        return self.fname + ' ' + self.lname


class EmployeeOrderBridge(models.Model):
    employee_ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='employee_ssn', primary_key=True)
    order_number = models.ForeignKey('Order', models.DO_NOTHING, db_column='order_number')
    hours = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'employee_order_bridge'
        unique_together = (('employee_ssn', 'order_number'),)


class Order(models.Model):
    order_num = models.IntegerField(primary_key=True)
    order_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'order'


class Product(models.Model):
    product_number = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    release_year = models.DateField()

    class Meta:
        managed = False
        db_table = 'product'


class ProductColor(models.Model):
    product_number = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_number')
    color = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'product_color'
        unique_together = (('color', 'product_number'),)


class ProductOrderBridge(models.Model):
    order_number = models.OneToOneField(Order, models.DO_NOTHING, db_column='order_number', primary_key=True)
    product_number = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_number')
    quantity = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'product_order_bridge'
        unique_together = (('order_number', 'product_number'),)


class Supplier(models.Model):
    supplier_number = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'supplier'


class SupplierPhone(models.Model):
    supplier_number = models.OneToOneField(Supplier, models.DO_NOTHING, db_column='supplier_number', primary_key=True)
    phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'supplier_phone'
        unique_together = (('supplier_number', 'phone'),)


class SupplierProductBridge(models.Model):
    supplier_number = models.OneToOneField(Supplier, models.DO_NOTHING, db_column='supplier_number', primary_key=True)
    product_number = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_number')
    phone = models.CharField(max_length=15)
    bought_date = models.DateField()
    supervisor = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'supplier_product_bridge'
        unique_together = (('supplier_number', 'product_number'),)
