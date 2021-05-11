from django import forms

from .models import SaleMST, SaleDTL, City, SaleRetMST, SaleRetDTL, PurchaseMST, PurchaseDTL, PurchaseRetMST, \
    PurchaseRetDTL, Customer, Vendor

"""
 Form used in City form
"""


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'})
        }


"""
 Form used in Customer form
"""


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'city': forms.Select(attrs={'class': 'form-control mb-2'})
        }


"""
 Form used in Vendor form
"""


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'phone', 'email', 'address', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'city': forms.Select(attrs={'class': 'form-control mb-2'})
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
 For used in Sale view and Edit sale view as well
"""


class SaleRetMSTForm(forms.ModelForm):
    class Meta:
        model = SaleRetMST
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
 From for sale view used for DTL model.
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
 From for sale view used for DTL Return Forms
"""


class SaleRetForm(forms.ModelForm):
    class Meta:
        model = SaleRetDTL
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

"""
 Formset for Edit sale Return view
"""

SaleRetDTLForm = forms.inlineformset_factory(SaleRetMST, SaleRetDTL, extra=0, fields=('mst', 'product', 'desc', 'qty',),
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

"""
 For used in Purchase view and Edit sale view as well
"""


class PurchaseMSTForm(forms.ModelForm):
    class Meta:
        model = PurchaseMST
        fields = ['vendor', 'date', 'desc', 'disc']
        widgets = {
            'vendor': forms.Select(attrs={
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
            'vendor': 'Vendor',
            'desc': 'Description',
            'disc': 'Discount'
        }


"""
 For used in Purchase view and Edit sale view as well
"""


class PurchaseRetMSTForm(forms.ModelForm):
    class Meta:
        model = PurchaseRetMST
        fields = ['vendor', 'date', 'desc', 'disc']
        widgets = {
            'vendor': forms.Select(attrs={
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
            'vendor': 'Vendor',
            'desc': 'Description',
            'disc': 'Discount'
        }


"""
 From for Purchase view used for DTL model.
"""


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseDTL
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
 From for Purchase view used for DTL Return Forms
"""


class PurchaseRetForm(forms.ModelForm):
    class Meta:
        model = PurchaseRetDTL
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
 Formset for Edit Purchase view
"""

PurchaseDTLForm = forms.inlineformset_factory(PurchaseMST, PurchaseDTL, extra=0,
                                              fields=('mst', 'product', 'desc', 'qty',),
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

"""
 Formset for Edit Purchase Return view
"""

PurchaseRetDTLForm = forms.inlineformset_factory(PurchaseRetMST, PurchaseRetDTL, extra=0,
                                                 fields=('mst', 'product', 'desc', 'qty',),
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
