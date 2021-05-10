from django import forms

from .models import SaleMST, SaleDTL, City

"""
 Form used in City view
"""


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'})
        }


"""
 For used in Sale view and Edit sale view as well
"""


class SaleMSTForm(forms.ModelForm):
    class Meta:
        model = SaleMST
        fields = ['customer', 'date', 'desc', 'disc']
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'desc': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'disc': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'customer': 'Customer',
            'desc': 'Description',
            'disc': 'Discount'
        }


"""
 From for sale view used for DTL model
"""


class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleDTL
        fields = ['mst', 'product', 'desc', 'qty']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'desc': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'qty': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            })
        }
        labels = {
            'product': 'Select Product',
            'desc': 'Description'
        }


"""
 Formset for Edit sale view
"""

SaleDTLForm = forms.inlineformset_factory(SaleMST, SaleDTL, extra=0, fields=('mst', 'product', 'desc', 'qty',),
                                          widgets={
                                              'product': forms.Select(attrs={
                                                  'class': 'form-control',
                                                  'required': True
                                              }),
                                              'desc': forms.TextInput(attrs={
                                                  'class': 'form-control'
                                              }),
                                              'qty': forms.TextInput(attrs={
                                                  'class': 'form-control'
                                              })
                                          })
