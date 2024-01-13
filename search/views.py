from search.forms import SearchForm
from pizza.models import Pizza
from burgers.models import Burger
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import View


class AdvancedSearchView(View):
    template_name = 'search/search.html'

    def get(self, request):
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
                filters = [name_search]
                rate_until = form.cleaned_data.get("rate_until")
                rate_from = form.cleaned_data.get("rate_from")
                calories_until = form.cleaned_data.get("calories_until")

                if rate_from is not "0":
                    filters.append(Q(rate__gte=rate_from))
                if rate_until is not "0":
                    filters.append(Q(rate__lte=rate_until))
                if calories_until is not None:
                    filters.append(Q(calories__lte=calories_until))

                result_product = product_table.objects.filter(*filters)

        return render(request, self.template_name, {"form": form, "result_product": result_product})