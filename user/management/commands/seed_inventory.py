from django.core.management.base import BaseCommand
from django.db import transaction

from user.models import Category, Brand, Manufacturer, Unit, Product


class Command(BaseCommand):
    help = 'Seed default categories, brands, manufacturers, units, and products.'

    @transaction.atomic
    def handle(self, *args, **options):
        categories_data = [
            {
                'categ_name': 'Electronics',
                'description': 'Devices, gadgets, and electronic accessories.',
                'categ_status': 'active',
            },
            {
                'categ_name': 'Office Supplies',
                'description': 'Paper, pens, and tools for the office.',
                'categ_status': 'active',
            },
            {
                'categ_name': 'Furniture',
                'description': 'Indoor and outdoor furniture for home and office.',
                'categ_status': 'active',
            },
            {
                'categ_name': 'Apparel',
                'description': 'Clothing and fashion accessories.',
                'categ_status': 'active',
            },
        ]

        brand_names = [
            'Acme',
            'Global Tech',
            'HomePro',
            'Fashion Hub',
        ]

        manufacturer_names = [
            'Acme Manufacturing',
            'Global Manufacturing',
            'HomePro Factory',
            'Fashion Hub Works',
        ]

        units_data = [
            {'unit_name': 'Piece', 'unit_symbol': 'pc'},
            {'unit_name': 'Box', 'unit_symbol': 'bx'},
            {'unit_name': 'Package', 'unit_symbol': 'pkg'},
            {'unit_name': 'Set', 'unit_symbol': 'set'},
        ]

        products_data = [
            {
                'product_name': 'Wireless Mouse',
                'category': 'Electronics',
                'brand': 'Acme',
                'manufacturer': 'Acme Manufacturing',
                'unit': 'Piece',
                'cost_price': '8.50',
                'sell_price': '15.00',
                'stock_qty': 120,
                'reorder_level': 20,
            },
            {
                'product_name': 'Office Chair',
                'category': 'Furniture',
                'brand': 'HomePro',
                'manufacturer': 'HomePro Factory',
                'unit': 'Piece',
                'cost_price': '25.00',
                'sell_price': '55.00',
                'stock_qty': 40,
                'reorder_level': 5,
            },
            {
                'product_name': 'Ballpoint Pen Set',
                'category': 'Office Supplies',
                'brand': 'Global Tech',
                'manufacturer': 'Global Manufacturing',
                'unit': 'Set',
                'cost_price': '3.00',
                'sell_price': '6.50',
                'stock_qty': 200,
                'reorder_level': 30,
            },
            {
                'product_name': 'Cotton T-Shirt',
                'category': 'Apparel',
                'brand': 'Fashion Hub',
                'manufacturer': 'Fashion Hub Works',
                'unit': 'Piece',
                'cost_price': '6.00',
                'sell_price': '12.99',
                'stock_qty': 80,
                'reorder_level': 10,
            },
        ]

        self.stdout.write('Seeding categories...')
        categories = {}
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(
                categ_name=category_data['categ_name'],
                defaults={
                    'description': category_data['description'],
                    'categ_status': category_data['categ_status'],
                },
            )
            categories[category.categ_name] = category
            self.stdout.write(self.style.SUCCESS(
                f"{category.categ_name} {'created' if created else 'already exists'}"
            ))

        self.stdout.write('Seeding brands...')
        brands = {}
        for name in brand_names:
            brand, created = Brand.objects.get_or_create(brand_name=name)
            brands[brand.brand_name] = brand
            self.stdout.write(self.style.SUCCESS(
                f"{brand.brand_name} {'created' if created else 'already exists'}"
            ))

        self.stdout.write('Seeding manufacturers...')
        manufacturers = {}
        for name in manufacturer_names:
            manufacturer, created = Manufacturer.objects.get_or_create(manufacturer_name=name)
            manufacturers[manufacturer.manufacturer_name] = manufacturer
            self.stdout.write(self.style.SUCCESS(
                f"{manufacturer.manufacturer_name} {'created' if created else 'already exists'}"
            ))

        self.stdout.write('Seeding units...')
        units = {}
        for unit_data in units_data:
            unit, created = Unit.objects.get_or_create(
                unit_name=unit_data['unit_name'],
                defaults={'unit_symbol': unit_data['unit_symbol']},
            )
            units[unit.unit_name] = unit
            self.stdout.write(self.style.SUCCESS(
                f"{unit.unit_name} {'created' if created else 'already exists'}"
            ))

        self.stdout.write('Seeding products...')
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                product_name=product_data['product_name'],
                defaults={
                    'category': categories[product_data['category']],
                    'brand': brands[product_data['brand']],
                    'manufacturer': manufacturers[product_data['manufacturer']],
                    'unit': units[product_data['unit']],
                    'cost_price': product_data['cost_price'],
                    'sell_price': product_data['sell_price'],
                    'stock_qty': product_data['stock_qty'],
                    'reorder_level': product_data['reorder_level'],
                    'is_active': True,
                },
            )
            self.stdout.write(self.style.SUCCESS(
                f"{product.product_name} {'created' if created else 'already exists'}"
            ))

        self.stdout.write(self.style.SUCCESS('Seeding completed.'))
