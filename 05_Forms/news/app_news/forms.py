from django import forms
from .models import News, Comment
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description']
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'description']
        help_texts = {
            'user': 'Введите имя пользователя',
            'description': 'Введите комментарий',
        }

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name', False)
        if user_name == '':
            raise ValidationError(
                _('Введите имя'),
                params={'value': user_name},
            )
        return user_name

    def clean_description(self):
        description = self.cleaned_data.get('description', False)
        if description == '':
            raise ValidationError(
                _('Введите описание'),
                params={'value': description},
            )
        return description