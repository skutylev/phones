from django.contrib.auth.models import User
from phones.models import Person
from django import forms


class CallForm(forms.Form):

    def get_callee(self):
        callee = User.objects.select_related('positioninunit__phone__number').filter(id=self.user)
        return callee

    caller = '922'
    login = 'DTF:0101571'
    password = '522677072'
