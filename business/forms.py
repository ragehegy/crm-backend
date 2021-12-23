from django import forms

from .models import DistrictEmplyoee, Employee, Unit

class BusinessUnitForm(forms.ModelForm):

    class Meta: 
        model = Unit
        fields = ('name',)


class DistrictEmployeesForm(forms.ModelForm):
    CHOICES = Employee.objects.values_list('id', 'first_name')

    employees = forms.MultipleChoiceField(
        choices=[*CHOICES], 
        required=False ,
        widget=forms.SelectMultiple, 
        initial=list(DistrictEmplyoee.objects.values_list('employee_id', flat=True),)
    )
    
    class Meta:
        model = DistrictEmplyoee
        fields = '__all__'