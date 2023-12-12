from search.forms import SearchForm
from pizza.models import Pizza
from burgers.models import Burger
from django.shortcuts import render
from django.db.models import Q

def advanced_search(request):
    form = SearchForm()
    result_product = []
    if name := request.GET.get("name"):
        form = SearchForm(request.GET)
        if request.GET.get("product_type") == "burger":
            product_table = Burger
            name_search = Q(burger_name__icontains=name)
        else:
            product_table = Pizza
            name_search = Q(pizza_name__icontains=name)
        if form.is_valid():
            result_product = product_table.objects.filter(
                name_search | (Q(
                    rate__lte=form.cleaned_data.get("rate_until") or 0
                ) & Q(rate__gte=form.cleaned_data.get("rate_from" or 0)))
                | Q(calories__lte=form.cleaned_data.get("calories_until") or 0)
            )
    return render(request, "search/search.html", {"form": form, "result_product": result_product})

