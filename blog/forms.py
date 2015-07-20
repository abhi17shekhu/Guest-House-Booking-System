from django import forms
from django.forms import ModelForm, Select
from django.utils.translation import ugettext_lazy as _ #used in labels and '_' is to save typings in the field
from .models import Pend
from django.forms.widgets import DateTimeInput
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Pend
        fields = ('gname', 'dept','bookin','roomsno','address','tele_no','email','purpose','categ','expad','expdd')
        guest_house_type = (
                   ('MG', 'Main Guest House'),
                   ('FG', 'Faculty Guest House'),
                   )
        widgets = {'bookin': Select(choices=guest_house_type),
                    'expad' : DateTimeInput(),
                    }
        labels = {
            "gname": _("Guest Name"),
            "dept": _("Department"),
            "bookin": _("Guest House Type"),
            "roomsno": _("No. of Rooms (Single/Double)"),
            "address": _("Guest Address"),
            "tele_no": _("Guest Telephone No."),
            "email": _("Guest Email"),
            "purpose": _("Purpose of Stay"),
            "categ": _("Category"),
            "expad": _("Expected Arrival Date"),
            "expdd": _("Expected Departure Date"),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

