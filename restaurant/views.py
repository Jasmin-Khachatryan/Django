from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from restaurant.models import Restaurant


def restaurant(request):
    restaurants = Restaurant.objects.all().order_by("pk")
    paginator = Paginator(restaurants, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "restaurant/restaurant.html", {"restaurants": page_obj})


def detail_page(request, pk):
    res_detail = get_object_or_404(Restaurant, pk=pk)
    return render(request, "restaurant/detail.html", {"restaurant": res_detail})


def burger_detail_page(request, pk):
    burger_detail = get_object_or_404(Restaurant, pk=pk)
    return render(request, "restaurant/burger_detail.html",{"restaurant":burger_detail})


