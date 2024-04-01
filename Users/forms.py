from django import forms

from Users.models import Userregister_Model


class Userregister_Form(forms.ModelForm):
    class Meta:
        model = Userregister_Model
        fields = ('name','email','password', 'phoneno', 'address', 'location')

