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

