from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView
from .models import Employee
from django import forms
from django.forms import extras
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy


START_YEAR = ('2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
              '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
YEAR_OF_BIRTH = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991',
                 '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
                 '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015')


class EmployeeCreateForm(forms.ModelForm):
    RACE_OPTIONS = (
        ('A', 'African'),
        ('W', 'White'),
        ('I', 'Indian'),
        ('C', 'Coloured'),
        ('O', 'Others'),
    )
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-md-12'}))
    id_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    tax_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    personal_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    github_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    physical_address = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control col-md-12'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_OPTIONS, attrs={'class': 'form-control col-md-12'}))
    race = forms.CharField(widget=forms.Select(choices=RACE_OPTIONS, attrs={'class': 'form-control col-md-12'}))
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=YEAR_OF_BIRTH, attrs={'class': 'form-control col-md-12'}))
    start_date = forms.DateField(widget=extras.SelectDateWidget(years=START_YEAR, attrs={'class': 'form-control col-md-12'}))

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateViewSet(SuccessMessageMixin, CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employee/employee_create_form.html'
    success_url = reverse_lazy('created')
    success_message = 'Review successfully updated'

    def get_success_message(self, cleaned_data):
        return self.success_message


class EmployeeListViewSet(ListView):
    model = Employee
    context_object_name = 'employees_object'
    fields = '__all__'
    template_name = 'employee/employee_list_form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListViewSet, self).get_context_data(**kwargs)
        return context


class EmployeeUpdateForm(forms.ModelForm):
    RACE_OPTIONS = (
        ('A', 'African'),
        ('W', 'White'),
        ('I', 'Indian'),
        ('C', 'Coloured'),
        ('O', 'Others'),
    )
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control col-md-12'}))
    id_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    tax_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    personal_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    github_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    physical_address = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control col-md-12'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_OPTIONS, attrs={'class': 'form-control col-md-12'}))
    race = forms.CharField(widget=forms.Select(choices=RACE_OPTIONS, attrs={'class': 'form-control col-md-12'}))
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=YEAR_OF_BIRTH, attrs={'class': 'form-control col-md-12'}))
    start_date = forms.DateField(widget=extras.SelectDateWidget(years=START_YEAR, attrs={'class': 'form-control col-md-12'}))

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeUpdateViewSet(UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    template_name = 'employee/employee_update_form.html'
    success_url = reverse_lazy('updated')
    success_message = 'Employee successfully updated'
