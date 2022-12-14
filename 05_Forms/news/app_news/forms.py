from django import forms
from .models import News, Comment, UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class ExtendedUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    phone = forms.CharField(max_length=10, required=False, label='Телефон')
    town = forms.CharField(max_length=10, required=False, label='Город')
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

    def save(self, commit=True):
        super().save()
        UserProfile.objects.create(user=User.objects.get(username=self.cleaned_data["username"]),
                                   phone=self.cleaned_data["phone"],
                                   town=self.cleaned_data["town"])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'town', 'password1', 'password2', )
        labels = {
            'username': _('Логин'),
        }
        help_texts = {
            'username': _('Буквы, цифры и @/./+/-/_'),
        }


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'tag']
        help_texts = {
            'title': 'Введите заголовок',
            'description': 'Введите описание',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', False)
        if title == '':
            raise ValidationError(
                _('Введите заголовок'),
                params={'value': title},
            )
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', False)
        if description == '':
            raise ValidationError(
                _('Введите описание'),
                params={'value': description},
            )
        return description


def get_comment_form(is_auth, data=None):
    if is_auth:
        if data is None:
            return LoggedCommentForm()
        else:
            return LoggedCommentForm(data)
    else:
        if data is None:
            return AnonimCommentForm()
        else:
            return AnonimCommentForm(data)


class LoggedCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        help_texts = {
            'description': 'Введите комментарий',
        }

    def clean_description(self):
        description = self.cleaned_data.get('description', False)
        if description == '':
            raise ValidationError(
                _('Введите описание'),
                params={'value': description},
            )
        return description


class AnonimCommentForm(forms.ModelForm):
    user = forms.CharField(label='Пользователь')
    class Meta:
        model = Comment
        fields = ['description']
        help_texts = {
            'description': 'Введите комментарий',
        }


    def clean_user(self):
        user = self.cleaned_data.get('user', False)
        if user == '':
            raise ValidationError(
                _('Введите имя'),
                params={'value': user},
            )
        return user

    def clean_description(self):
        description = self.cleaned_data.get('description', False)
        if description == '':
            raise ValidationError(
                _('Введите описание'),
                params={'value': description},
            )
        return description

