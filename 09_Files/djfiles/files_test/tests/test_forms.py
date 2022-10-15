from django.test import TestCase
from ..forms import UserPageForm, RecordForm


class UserPageFormTest(TestCase):

    def test_form(self):
        form_data = {'first_name': 'wdgfsdfgdf',
                     'last_name': 'afsdfsda',
                     'about': 'sdfsdf'}
        form = UserPageForm(data=form_data)
        self.assertTrue(form.is_valid())


class RecordFormTest(TestCase):

    def test_form(self):
        form_data = {'description': 'wdgfsdfgdf'}
        form = RecordForm(data=form_data)
        self.assertTrue(form.is_valid())