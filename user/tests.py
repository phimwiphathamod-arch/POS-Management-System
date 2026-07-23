from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Brand, Cart, CartItem, Category, Manufacturer, Product, Unit


class AddToCartTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@example.com',
            password='password123',
        )
        self.category = Category.objects.create(categ_name='Electronics')
        self.brand = Brand.objects.create(brand_name='TestBrand')
        self.manufacturer = Manufacturer.objects.create(manufacturer_name='TestManufacturer')
        self.unit = Unit.objects.create(unit_name='pcs', unit_symbol='pcs')
        self.product = Product.objects.create(
            product_name='Keyboard',
            category=self.category,
            brand=self.brand,
            manufacturer=self.manufacturer,
            unit=self.unit,
            cost_price=100,
            sell_price=150,
            stock_qty=10,
        )

    def test_add_to_cart_for_authenticated_user_creates_cart_item(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))

        self.assertRedirects(response, reverse('cart'))
        self.assertEqual(Cart.objects.filter(user=self.user).count(), 1)
        self.assertEqual(
            CartItem.objects.filter(cart__user=self.user, product=self.product).count(),
            1,
        )

    def test_add_to_cart_for_anonymous_user_redirects_to_login(self):
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))

        self.assertRedirects(response, reverse('login'))
