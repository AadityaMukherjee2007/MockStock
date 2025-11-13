from email.policy import default
from logging import PlaceHolder
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.http import JsonResponse

from .models import Team, Company

# Create your views here.

class PriceUpdateForm(forms.Form):
    price = forms.DecimalField(
        min_value=0,
        decimal_places=2,
        label="Current Price",
        widget=forms.NumberInput(
            attrs={
                "id": "update_price",
                "class": "border p-2 rounded shadow-md w-40 text-center",
                "placeholder": "Enter new price",
            }
        )
    )

class ShareAllocationForm(forms.Form):
    shares = forms.IntegerField(
        min_value=0,
        label="",
        widget=forms.NumberInput(
            attrs={
                "id": "allocate_shares",
                "class": "border px-2 py-1 m-2 rounded shadow-md  w-32 text-center",
                "placeholder": "Enter shares",
            }
        )
    )


def index(request):
    return HttpResponseRedirect(reverse("login"))


def login_view(request):
    companies = Company.objects.all()
    return render(request, "Stock/login.html", {
        "companies": companies
    })


def company_interface(request, company_name):
    # print(company_name)

    if company_name == "Admin":
        return render(request, "Stock/admin.html")

    company_data = Company.objects.get(name=company_name)

    return render(request, "Stock/company_interface.html", {
        "CompanyData": company_data,
        "Teams": Team.objects.all(),
        "price_form": PriceUpdateForm(initial={'price': company_data.curVal}),
        "share_alloc_form": ShareAllocationForm()
    })

def admin_interface(request):
    return render(request, "Stock/company_interface.html", {
        "CompanyData": Company.objects.all(),
        "Teams": Team.objects.all()
    })


def share_price_update(request):
    updated_price = request.GET.get("updated_price")
    company = request.GET.get("company")
    # print(company, updated_price)

    company_data = Company.objects.get(id=company)
    old_price = company_data.curVal
    company_data.curVal = updated_price
    company_data.save()

    if float(old_price) == float(updated_price):
        return JsonResponse({
            "message": "No Change"
        })

    return JsonResponse({
        "message": "Updated"
    })


# def allocate_shares(request):
