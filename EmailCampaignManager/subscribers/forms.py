from django import forms
from .models import Subscriber


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('first_name', 'email',)


class UnsubscribeForm(forms.Form):

    email = forms.EmailField(max_length=254)
