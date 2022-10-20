from django.test import TestCase
from django.urls import reverse


class ShopsListViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/shops-list')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('shops-list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/shops_list.html')

    def test_answer_code(self):
        url = reverse('shops-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class RegistrationViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/registration')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('registration')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/registration.html')

    def test_answer_code(self):
        url = reverse('registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class UserPageViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/user-page')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('user-page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/user_page.html')

    def test_answer_code(self):
        url = reverse('user-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ShopProductsViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/shop-products')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('shop-products')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/shop_products.html')

    def test_answer_code(self):
        url = reverse('shop-products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ProductDetailsViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/product-details')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('product-details')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/product_details.html')

    def test_answer_code(self):
        url = reverse('product-details')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)