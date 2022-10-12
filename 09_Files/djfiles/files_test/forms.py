from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Record
from django.core.exceptions import ValidationError
from .models import UserProfile


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class RecordsLoadForm(forms.Form):
    file = forms.FileField()


class UserPageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'about']
        help_texts = {
            'first_name': 'Введите имя',
            'last_name': 'Введите фамилию',
            'about': 'Добавьте информацию о себе'
        }


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="Минимум 8 знаков",
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Введите пароль ещё раз"),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        labels = {
            'username': _('Логин'),
        }
        help_texts = {
            'username': _('Буквы, цифры и @/./+/-/_'),
        }


class RecordForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Record
        fields = ['description']
        help_texts = {
            'description': 'Введите описание',
        }

    def clean_description(self):
        description = self.cleaned_data.get('description', False)
        if description == '':
            raise ValidationError(
                _('Введите описание'),
                params={'value': description},
            )
        return description

