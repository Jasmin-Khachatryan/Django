from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from burgers.models import Burger


def burger(request):
    burgers = Burger.objects.all()
    paginator = Paginator(burgers, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "burger/burger.html", {"burgers": page_obj})


def burger_info(request, pk):
    burgers_info = get_object_or_404(Burger, pk=pk)
    return render(request, "burger/burger_info.html", {"burgers": burgers_info})

