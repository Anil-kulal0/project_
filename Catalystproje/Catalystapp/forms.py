from django import forms
from .models import UploadedData, DataRecord

class UploadFileForm(forms.ModelForm):
      class Meta:
            model = UploadedData
            fields = ['data_file']

class DataFilterForm(forms.Form):
      keyword = forms.CharField(max_length=25)
      city = forms.CharField(max_length=25)
      employees_from = forms.CharField()
      industry = forms.CharField(max_length=50)
      state = forms.CharField(max_length=200)
      employees_to = forms.CharField()
      year_founded = forms.IntegerField()
      country = forms.CharField()
      


class LoginForm(forms.Form):
      username = forms.CharField(max_length=255)
      password = forms.CharField()
      
class DataRecordForm(forms.ModelForm):
      class  Meta:
            model =  DataRecord 
            fields = ['keyword', 'city', 'employees_from', 'industry', 
            'state', 'employees_to', 'year_founded','country'
            ]  


                  