from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm


class MultiDBAdminForm(AdminAuthenticationForm):
    database = forms.ChoiceField(choices=[], required=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields["database"].choices = [(k, k) for k in settings.DATABASES.keys()]


admin.site.login_form = MultiDBAdminForm
