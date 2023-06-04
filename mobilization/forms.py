from django import forms
from .models import Person, FamilyMember

#class PersonCustomForm(forms.ModelForm):
    #birthday = forms.DateField(input_formats=['%d/%m/%Y'], widget = forms.TextInput(attrs= {'autocomplete': 'off'}))



class PersonCustomForm(forms.ModelForm):
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d/%m/%Y', attrs={'autocomplete' : 'off'}), input_formats=['%d/%m/%Y'])
    statusdate = forms.DateField(label='Дата получения статуса', widget=forms.DateInput(format='%d/%m/%Y', attrs={'autocomplete' : 'off'}), input_formats=['%d/%m/%Y'])
    class Meta:
        model = Person
        fields = ('firstname', 'lastname', 'fathername', 'birthday', 'status', 'statusdate', 'otherdata')


class FamilyMemberCustomForm(forms.ModelForm):
    memberbirthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d/%m/%Y', attrs={'autocomplete' : 'off'}), input_formats=['%d/%m/%Y'])
    class Meta:        
        model = FamilyMember
        fields = ('memberfirstname', 'memberlastname', 'memberfathername', 'memberbirthday', 'social', 'relation', 'phonenumber', 'memberotherdata', 'index', 'city', 'street', 'building', 'apartment')


