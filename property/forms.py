from django import forms

from .models import PropertyBook

    # date_from = models.DateField(default=timezone.now)
    # date_to = models.DateField(default=timezone.now)
    # guest = models.CharField(max_length=2, choices=COUNT)
    # children = models.CharField(max_length=2, choices=COUNT)
    

class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))
    date_to = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest', 'children']