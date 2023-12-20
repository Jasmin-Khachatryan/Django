from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from burgers.models import Burger
from burgers.forms import BurgerForm
from django.contrib import messages


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

def add_burger(request):
    form = BurgerForm()

    if request.method == "POST":
        form = BurgerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect("burgers")


    return render(request, "burger/add_burger.html", {"form": form})


def update_burger(request, pk: int):
    burger = get_object_or_404(Burger, pk=pk)
    form = BurgerForm(instance=burger)
    if request.method == "POST":
        form = BurgerForm(request.POST, request.FILES, instance=burger)
        if form.is_valid():
            burger_upd = form.save()
            messages.info(request, "Burger was updated successfully!")

            return redirect(burger_upd)
    return render(request, "burger/burger_update.html", {"form": form})


def delete_burger(request, pk: int):
    burger = get_object_or_404(Burger, pk=pk)
    if request.method == "POST":
        burger.delete()
        messages.error(request, "Burger was deleted successfully!")
        return redirect("burgers")
    return render(request, "burger/burger_delete.html", {"burger": burger})
