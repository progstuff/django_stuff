from django.test import TestCase
from django.urls import reverse


class AllPostsPageTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/all-posts')
        self.assertEqual(response.status_code, 200)

    def test_template_exist(self):
        url = reverse('all-posts')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'files_test/all_posts.html')

    def test_all_posts_answer_code(self):
        url = reverse('all-posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class LoginPageTest(TestCase):

    def test_template_exist(self):
        url = reverse('login-user')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'files_test/login_page.html')

    def test_url_exist(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_answer_code(self):
        url = reverse('login-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contains_elements(self):
        url = reverse('login-user')
        response = self.client.get(url)
        self.assertContains(response, 'На главную')
        self.assertContains(response, 'Вход')


class LogoutPageTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)

    def test_answer_code(self):
        url = reverse('logout-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class RegisterPageTest(TestCase):

    def test_template_exist(self):
        url = reverse('register-user')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'files_test/register_page.html')

    def test_url_exist(self):
        response = self.client.get('/register-user')
        self.assertEqual(response.status_code, 200)

    def test_answer_code(self):
        url = reverse('register-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contains_elements(self):
        url = reverse('register-user')
        response = self.client.get(url)
        self.assertContains(response, 'На главную')
        self.assertContains(response, 'Отправить')


class UserPageTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/user-page')
        self.assertEqual(response.status_code, 302)

    def test_answer_code(self):
        url = reverse('user-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class PostCreatePageTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/create-post')
        self.assertEqual(response.status_code, 302)

    def test_answer_code(self):
        url = reverse('create-post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class CreateSeveralPostsPageTest(TestCase):

    def test_url_exist(self):
        response = self.client.get('/create-several-posts')
        self.assertEqual(response.status_code, 302)

    def test_answer_code(self):
        url = reverse('create-several-posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)