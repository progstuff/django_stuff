from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_("Минимум 8 знаков"),
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