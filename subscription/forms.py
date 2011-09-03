#-*- coding: utf-8 -*-
from django import forms
from subscription.models import Subscription
from subscription.validators import CpfValidator
from django.core.validators import EMPTY_VALUES

class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None, None]

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in EMPTY_VALUES:
                raise forms.ValidationError(u'DDD inválido.')
            if data_list[1] in EMPTY_VALUES:
                raise forms.ValidationError(u'Número inválido.')
            return '%s-%s' % tuple(data_list)
        return None
    
class SubscriptionForm(forms.ModelForm):
    fone = PhoneField(required=False)
    class Meta:
        model = Subscription
        exclude = ('criado_em', 'pago')
    
    def clean(self):  
        super(SubscriptionForm,self).clean()
        if not self.cleaned_data.get('email') and \
          not self.cleaned_data.get('fone'):
            raise forms.ValidationError(
                (u'Informe seu e-­‐mail ou telefone.'))
        return self.cleaned_data

#class SubscriptionForm(forms.Form):
#    nome = forms.CharField(max_length=100)
#    cpf = forms.CharField(max_length=11, min_length=11, validators=[CpfValidator])
#    email = forms.EmailField(label=('E-mail'),required = False)
#    telefone = forms.CharField(required = False, max_length=20)
#    
#    def _unique_check(self, fieldname, error_message):
#        param = { fieldname: self.cleaned_data[fieldname] }
#        try:
#            s = Subscription.objects.get(**param)
#        except Subscription.DoesNotExist:
#            return self.cleaned_data[fieldname]
#        raise forms.ValidationError(error_message)
#    
#    def clean_cpf(self):
#        return self._unique_check('cpf', (u'CPF já inscrito.'))
#
#    def clean_email(self):
#        return self._unique_check('email', (u'E-mail já inscrito.'))
#    
#    def clean(self):
#        if not self.cleaned_data.get('email') and \
#           not self.cleaned_data.get('telefone'):
#                error_message = (u'Você precisa informar seu e-mail ou seu telefone.')
#                raise forms.ValidationError(error_message)
#        return self.cleaned_data



