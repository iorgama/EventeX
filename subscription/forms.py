from django import forms
from subscription.models import *

class SubscriptionForm(forms.ModelForm):
  class Meta:
      model = Subscription
      exclude = ('criado_em',)
