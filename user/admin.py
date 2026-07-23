from django.contrib import admin

from .models import (
    CustomUser,
    Category,
    Product,
    Brand,
    Manufacturer,
    Unit,
    Supplier,
    Warehouse,
    Inventory,
    UserType,
    FunctionMenu,
)


# CATEGORY
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categ_name',
        'categ_status',
        'created_at'
    )

    search_fields = (
        'categ_name',
    )

    list_filter = (
        'categ_status',
    )


# PRODUCT
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product_name',
        'category',
        'brand',
        'sell_price',
        'stock_qty',
        'is_active'
    )

    search_fields = (
        'product_name',
    )

    list_filter = (
        'category',
        'brand',
        'is_active'
    )


# BRAND
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'brand_name',
        'created_at'
    )

    search_fields = (
        'brand_name',
    )


# MANUFACTURER
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'manufacturer_name',
        'created_at'
    )

    search_fields = (
        'manufacturer_name',
    )


# UNIT
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'unit_name',
        'unit_symbol'
    )

    search_fields = (
        'unit_name',
    )


# SUPPLIER
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'supplier_name',
        'phone',
        'email'
    )

    search_fields = (
        'supplier_name',
        'phone'
    )


# WAREHOUSE
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'warehouse_name',
        'location'
    )

    search_fields = (
        'warehouse_name',
    )


# INVENTORY
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product',
        'warehouse',
        'quantity_on_hand',
        'quantity_reserved'
    )

    list_filter = (
        'warehouse',
    )


# USER
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'username',
        'users_role',
        'user_status',
        'is_active'
    )

    list_filter = (
        'users_role',
        'user_status'
    )

    search_fields = (
        'username',
        'email'
    )


# USER TYPE
@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'typename',
        'status'
    )
    
# FUNCTION MENU
@admin.register(FunctionMenu)
class FunctionMenuAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'code',
        'fname',
        'status'
    )