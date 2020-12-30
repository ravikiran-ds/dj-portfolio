from django import forms
from my_portfolio.models import Msg

class InfoForm(forms.ModelForm):
    class Meta:
        model=Msg
        fields="__all__"
        widgets={'name':forms.TextInput(attrs={"title":"Your Name :"})}
