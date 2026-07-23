from django.db import models
from django.contrib.auth.models import AbstractUser

#UserType #Role
class UserType(models.Model):
     
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    typename = models.CharField(max_length = 50)
    function = models.CharField(max_length = 255) # เก็บสิทธิ์แบบ 001,002,003

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.typename

# Function Menu
class FunctionMenu(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    code = models.CharField(max_length = 50)
    fname = models.CharField(max_length = 50)
    furl = models.CharField(max_length = 50)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
    ]

    email = models.EmailField(
        unique=True
    )

    users_role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    user_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    address = models.TextField(
    blank=True,
    null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        # superuser = admin
        if self.is_superuser:
            self.users_role = 'admin'

        super().save(*args, **kwargs)
        
# Product Category
class Category(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    categ_name = models.CharField(max_length = 50)
    description = models.TextField(
        blank = True,
        null = True
    )
    categ_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.categ_name

# BRAND
class Brand(models.Model):

    brand_name = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.brand_name

# MANUFACTURER
class Manufacturer(models.Model):

    manufacturer_name = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.manufacturer_name



# UNIT
class Unit(models.Model):

    unit_name = models.CharField(
        max_length=50
    )

    unit_symbol = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.unit_name


# PRODUCT
class Product(models.Model):

    product_name = models.CharField(
        max_length=100
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products'
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='products'
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    sell_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    stock_qty = models.IntegerField(
        default=0
    )

    reorder_level = models.IntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.product_name


# SUPPLIER
class Supplier(models.Model):

    supplier_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.supplier_name


# WAREHOUSE
class Warehouse(models.Model):

    warehouse_name = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.warehouse_name



# INVENTORY
class Inventory(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='inventories'
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='inventories'
    )

    quantity_on_hand = models.IntegerField(
        default=0
    )

    quantity_reserved = models.IntegerField(
        default=0
    )

    average_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.product_name} - {self.warehouse.warehouse_name}"
    

class Cart(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="carts"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"

class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.sell_price * self.quantity

    def __str__(self):
        return self.product.product_name
    
class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancel', 'Cancel'),
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.product.product_name