from django.core.paginator import Paginator
from django.shortcuts import render

from burgers.models import Burger


def burger(request):
    burgers = Burger.objects.all()
    paginator = Paginator(burgers, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "burger/burger.html", {"burgers": page_obj})



