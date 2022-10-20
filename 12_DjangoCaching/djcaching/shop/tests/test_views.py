from django.test import TestCase
from django.urls import reverse


class ShopsListViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/shops-list')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('shops-list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/page_shops_list.html')

    def test_answer_code(self):
        url = reverse('shops-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_language_form_exist(self):
        url = reverse('shops-list')
        response = self.client.get(url)
        self.assertContains(response, '<select name="language">')


class RegistrationViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/registration')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('registration')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/page_registration.html')

    def test_answer_code(self):
        url = reverse('registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_language_form_exist(self):
        url = reverse('registration')
        response = self.client.get(url)
        self.assertContains(response, '<select name="language">')


class UserPageViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/user-page')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('user-page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/page_user.html')

    def test_answer_code(self):
        url = reverse('user-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_language_form_exist(self):
        url = reverse('user-page')
        response = self.client.get(url)
        self.assertContains(response, '<select name="language">')


class ShopProductsViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/shop-products')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('shop-products')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/page_shop_products.html')

    def test_answer_code(self):
        url = reverse('shop-products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_language_form_exist(self):
        url = reverse('shop-products')
        response = self.client.get(url)
        self.assertContains(response, '<select name="language">')


class ProductDetailsViewTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/product-details')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('product-details')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shop/page_product_details.html')

    def test_answer_code(self):
        url = reverse('product-details')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_language_form_exist(self):
        url = reverse('product-details')
        response = self.client.get(url)
        self.assertContains(response, '<select name="language">')