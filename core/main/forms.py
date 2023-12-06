from django import forms
from .models import Reservation

class ReservationModelForm(forms.ModelForm):

    class Meta:

        model = Reservation
        fields = ['res_name', 'res_lastname', 'res_phone', 'res_email', 'res_date', 'res_time']