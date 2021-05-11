import sweetify
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from .forms import CityForm, SaleMSTForm, SaleDTLForm, SaleForm, SaleRetMSTForm, SaleRetDTLForm, SaleRetForm, \
    PurchaseMSTForm, PurchaseForm, PurchaseDTLForm, PurchaseRetMSTForm, PurchaseRetForm, PurchaseRetDTLForm, \
    CustomerForm, VendorForm
from .models import SaleMST, SaleDTL, SaleRetMST, SaleRetDTL, PurchaseMST, PurchaseDTL, PurchaseRetMST, PurchaseRetDTL

"""
Views file for Core App
"""


def index(request):
    pk = SaleMST.objects.all().order_by('-id')[0].pk
    err = sweetify.error(request, 'Document deleted.')
    print(pk)
    print(err)
    return render(request, 'core/index.html')


def cities(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            modal_instance = form.save()
            mst = modal_instance.pk
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            sweetify.success(request, 'Success', text=msg,
                             persistent='OK')
            return redirect('cities')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'form': form
    }

    return render(request, 'core/cities.html', context)


def customer(request):
    form = CustomerForm()
    temp_name = "Customer"

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            modal_instance = form.save()
            mst = modal_instance.pk
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            sweetify.success(request, 'Success', text=msg,
                             persistent='OK')
            return redirect('customer')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'form': form,
        'temp_name': temp_name,
    }

    return render(request, 'core/profile.html', context)


def vendor(request):
    form = VendorForm()
    temp_name = "Vendor"

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            modal_instance = form.save()
            mst = modal_instance.pk
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            sweetify.success(request, 'Success', text=msg,
                             persistent='OK')
            return redirect('vendor')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'form': form,
        'temp_name': temp_name,
    }

    return render(request, 'core/profile.html', context)


def sale(request):
    m_form = SaleMSTForm()
    d_form = inlineformset_factory(SaleMST, SaleDTL, SaleForm, extra=2)
    temp_name = "Sale"

    if request.method == 'POST':
        m_form = SaleMSTForm(request.POST)
        if m_form.is_valid():
            modal_instance = m_form.save()
            mst = modal_instance.pk
            mstf = SaleMST.objects.get(id=mst)
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            formset = d_form(request.POST, instance=mstf)

            if formset.is_valid():
                # formset.save(commit=False)
                formset.save()
                sweetify.success(request, 'Success', text=msg,
                                 persistent='OK')
                return redirect('sale')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)


def edit_sale(request, pk):
    sale_query = SaleMST.objects.get(id=pk)
    m_form = SaleMSTForm(instance=sale_query)
    d_form = SaleDTLForm(instance=sale_query)
    temp_name = "Edit Sale"

    if request.method == 'POST':
        m_form = SaleMSTForm(request.POST, instance=sale_query)
        if m_form.is_valid():
            m_form.save()
            formset = SaleDTLForm(request.POST, instance=sale_query)

            if formset.is_valid():
                formset.save()
                sweetify.success(request, 'Success', text="Invoice has been updated successfully!",
                                 persistent='OK')
                return redirect('sale')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)


def sale_return(request):
    m_form = SaleRetMSTForm()
    d_form = inlineformset_factory(SaleRetMST, SaleRetDTL, SaleRetForm, extra=2)
    temp_name = "Sale Return"

    if request.method == 'POST':
        m_form = SaleRetMSTForm(request.POST)
        if m_form.is_valid():
            modal_instance = m_form.save()
            mst = modal_instance.pk
            mstf = SaleRetMST.objects.get(id=mst)
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            formset = d_form(request.POST, instance=mstf)

            if formset.is_valid():
                formset.save()
                sweetify.success(request, 'Success', text=msg,
                                 persistent='OK')
                return redirect('sale_return')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)


def edit_sale_return(request, pk):
    sale_query = SaleRetMST.objects.get(id=pk)
    m_form = SaleRetMSTForm(instance=sale_query)
    d_form = SaleRetDTLForm(instance=sale_query)
    temp_name = "Edit Sale Retuern"

    if request.method == 'POST':
        m_form = SaleRetMSTForm(request.POST, instance=sale_query)
        if m_form.is_valid():
            m_form.save()
            formset = SaleRetDTLForm(request.POST, instance=sale_query)

            if formset.is_valid():
                formset.save()
                sweetify.success(request, 'Success', text="Invoice has been updated successfully!",
                                 persistent='OK')
                return redirect('sale_return')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)


def purchase(request):
    m_form = PurchaseMSTForm()
    d_form = inlineformset_factory(PurchaseMST, PurchaseDTL, PurchaseForm, extra=2)
    temp_name = "Purchase"

    if request.method == 'POST':
        m_form = PurchaseMSTForm(request.POST)
        if m_form.is_valid():
            modal_instance = m_form.save()
            mst = modal_instance.pk
            mstf = PurchaseMST.objects.get(id=mst)
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            formset = d_form(request.POST, instance=mstf)

            if formset.is_valid():
                # formset.save(commit=False)
                formset.save()
                sweetify.success(request, 'Success', text=msg,
                                 persistent='OK')
                return redirect('purchase')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'form': m_form,
        'formset': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale_form.html', context)


def edit_purchase(request, pk):
    sale_query = PurchaseMST.objects.get(id=pk)
    m_form = PurchaseMSTForm(instance=sale_query)
    d_form = PurchaseDTLForm(instance=sale_query)
    temp_name = "Edit Purchase"

    if request.method == 'POST':
        m_form = PurchaseMSTForm(request.POST, instance=sale_query)
        if m_form.is_valid():
            m_form.save()
            formset = PurchaseDTLForm(request.POST, instance=sale_query)

            if formset.is_valid():
                formset.save()
                sweetify.success(request, 'Success', text="Invoice has been updated successfully!",
                                 persistent='OK')
                return redirect('purchase')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)


def purchase_return(request):
    m_form = PurchaseRetMSTForm()
    d_form = inlineformset_factory(PurchaseRetMST, PurchaseRetDTL, PurchaseRetForm, extra=2)
    temp_name = "Purchase Return"

    if request.method == 'POST':
        m_form = PurchaseRetMSTForm(request.POST)
        if m_form.is_valid():
            modal_instance = m_form.save()
            mst = modal_instance.pk
            mstf = PurchaseRetMST.objects.get(id=mst)
            msg = 'Invoice #' + str(mst) + ' has been created successfuly!'
            formset = d_form(request.POST, instance=mstf)

            if formset.is_valid():
                formset.save()
                sweetify.success(request, 'Success', text=msg,
                                 persistent='OK')
                return redirect('purchase_return')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)


def edit_purchase_return(request, pk):
    sale_query = PurchaseRetMST.objects.get(id=pk)
    m_form = PurchaseRetMSTForm(instance=sale_query)
    d_form = PurchaseRetDTLForm(instance=sale_query)
    temp_name = "Edit Purchase Retuern"

    if request.method == 'POST':
        m_form = PurchaseRetMSTForm(request.POST, instance=sale_query)
        if m_form.is_valid():
            m_form.save()
            formset = PurchaseRetDTLForm(request.POST, instance=sale_query)

            if formset.is_valid():
                formset.save()
                sweetify.success(request, 'Success', text="Invoice has been updated successfully!",
                                 persistent='OK')
                return redirect('purchase_return')
        else:
            msg = 'An error has been occured!'
            sweetify.error(request, 'Error', text=msg, persistent='OK')

    context = {
        'm_form': m_form,
        'd_form': d_form,
        'temp_name': temp_name,
    }

    return render(request, 'core/sale.html', context)
