from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django import forms

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
                "class": "border p-2 rounded shadow-md focus:ring-2 focus:ring-blue-400 w-40 text-center",
                "placeholder": "Enter new price",
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
    updatedForm = PriceUpdateForm(initial={'price': company_data.curVal})

    return render(request, "Stock/company_interface.html", {
        "CompanyData": company_data,
        "Teams": Team.objects.all(),
        "price_form": updatedForm
    })

def admin_interface(request):
    return render(request, "Stock/company_interface.html", {
        "CompanyData": Company.objects.all(),
        "Teams": Team.objects.all()
    })