from __future__ import absolute_import

import warnings

from django import forms

from django.utils.translation import pgettext, ugettext_lazy as _, ugettext


from rest_example.models import MyUser


class PasswordField(forms.CharField):

    def __init__(self, *args, **kwargs):

        kwargs['widget'] = forms.PasswordInput(render_value=False,attrs={'placeholder':_('Password')})
        super(PasswordField, self).__init__(*args, **kwargs)


class SetPasswordField(PasswordField):

    def clean(self, value):
        value = super(SetPasswordField, self).clean(value)
        return value


class SignupForm(forms.Form):

    username = forms.CharField(label=_("Username"),
                               max_length=30,
                               widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Username'),
                                          'autofocus': 'autofocus'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': _('E-mail address')}))

    password1 = SetPasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))
    confirmation_key = forms.CharField(max_length=40,
                                       required=False,
                                       widget=forms.HiddenInput())
    specialname = forms.CharField(label=_("Specialname"),
                               max_length=30)
    details = forms.CharField(label=_("Details"),
                               max_length=30)

    def save(self, request):
      
        user  = MyUser()
        data = self.cleaned_data
       
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
       
        user.username = data.get('username')
        user.email = data.get('email')
        user.specialname = data.get('specialname')
        user.details = data.get('details')
        user.save()
        return user
        
        

        


    