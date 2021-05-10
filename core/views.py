import sweetify
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import CityForm, SaleMSTForm, SaleDTLForm, SaleForm
from .models import SaleMST, SaleDTL

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
    c_form = CityForm()

    if request.method == 'POST':
        c_form = CityForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('cities')

    context = {
        'form': c_form
    }

    return render(request, 'core/cities.html', context)


def sale(request):
    m_form = SaleMSTForm()
    # d_form = SaleDTLForm
    d_form = inlineformset_factory(SaleMST, SaleDTL, SaleForm, extra=2)

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
    }

    return render(request, 'core/sale_form.html', context)


def edit_sale(request, pk):
    sale_query = SaleMST.objects.get(id=pk)
    m_form = SaleMSTForm(instance=sale_query)
    d_form = SaleDTLForm(instance=sale_query)

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
        'd_form': d_form
    }

    return render(request, 'core/sale_form.html', context)

# def form(request):
#     form_m = SaleMSTForm()
#     form_d = SaleDTLForm()
#
#     context = {
#         "form_m": form_m,
#         "form_d": form_d,
#     }
#
#     return render(request, 'core/form.html', context)
