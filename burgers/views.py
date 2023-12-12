from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from burgers.models import Burger


def burger(request):
    burgers = Burger.objects.all()
    paginator = Paginator(burgers, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "burger/burger.html", {"burgers": page_obj})


def burger_info(request, pk):
    reference_burger = get_object_or_404(Burger, pk=pk)

    price_range = 30
    calories_range = 40

    similar_burgers = Burger.objects.filter(
        Q(price__range=(reference_burger.price - price_range, reference_burger.price + price_range)) |
        Q(calories__range=(reference_burger.calories - calories_range, reference_burger.calories + calories_range))
    ).exclude(id=pk)

    context = {
        'burgers': reference_burger,
        'all_burger': similar_burgers,
    }

    return render(request, 'burger/burger_info.html', context)

