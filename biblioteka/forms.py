from django import forms
from django.core.validators import MaxValueValidator
from .validators import validate_rok

class NaszForm(forms.Form):
    imie = forms.CharField(label = 'Imie', max_length = 20)
    rok = forms.IntegerField(validators=[validate_rok])
    # rok = forms.IntegerField(validators=[MaxValueValidator(2020)])

    # def clean(self): #funkcja sprawdzająca czy rok spełnia jakieś warunki, mozna dac np. clean_rok(self) zeby wywolac funkcje tylko dla jednego pola
    #     cleaned_data = super(NaszForm, self).clean() 
    #     rok = self.cleaned_data.get('rok') #cleaned data - sprawdzone dane
    #     if rok > 2020:
    #         raise forms.ValidationError("Rok jest większy niż 2020")
    #     return rok

#własny validator:
    # def clean(self):
    #     cleaned_data = super(NaszForm, self).clean() 
    #     return validate_rok(cleaned_data.get('rok'))

