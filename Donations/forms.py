from django import forms
from .models import *

REQUEST_REASONS = (

    ('poor', 'Poor'),
    ('medicalEmergency', 'medical Emergency'),
    ('others', 'Others')
)


class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        exclude = ('user',)
        # fields = ('requesterFirstName','requesterLastName','requesterAddress','requesterCity','requesterZip','requesterNID',
        # 'requestDescription','requestReason','requestDocument','requestedAmount')


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ('user',)


class ZakatForm(forms.ModelForm):

    # firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'flex:5'}))
    # lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'flex:5'}))
    # address = forms.Textarea(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'flex:5'}))
    # phone = forms.TextInput(attrs={'class': 'form-control', 'style': 'flex:5'})
    # zakatAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'flex:5'}))
    # organization = forms.TextInput(widget=forms.Select(attrs={'class': 'form-control', 'style': 'flex:5'}))

    class Meta:
        model = Zakat
        exclude = ('user',)

