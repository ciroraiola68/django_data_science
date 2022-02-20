from django import forms
from matplotlib.pyplot import cla
from .models import Csv

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ['file_name']
