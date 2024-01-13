from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from burgers.models import Burger
from burgers.forms import BurgerForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BurgerListView(ListView):
    model = Burger
    paginate_by = 2
    template_name = "burger/burger.html"
    context_object_name = "burgers"


class BurgerDetailView(DetailView):
    template_name = "burger/burger_info.html"
    price_range = 30
    calories_range = 40

    def get(self, request, pk):
        reference_burger = get_object_or_404(Burger, pk=pk)
        similar_burgers = Burger.objects.filter(
            Q(price__range=(reference_burger.price - self.price_range, reference_burger.price + self.price_range)) |
            Q(calories__range=(reference_burger.calories - self.calories_range, reference_burger.calories +
                               self.calories_range))
        ).exclude(id=pk)

        context = {
            "burgers": reference_burger,
            "all_burger": similar_burgers,
        }

        return render(request, self.template_name, context)


class CreateBurgerView(CreateView):
    form_class = BurgerForm
    template_name = "burger/add_burger.html"
    context_object_name = "form"
    success_url = reverse_lazy("burgers")

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, "Burger was created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("burgers")


class UpdateBurgerView(UpdateView):
    model = Burger
    form_class = BurgerForm
    template_name = "burger/burger_update.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Burger was updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("burger_info", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Burger.objects.all()


class DeleteBurgerView(DeleteView):
    model = Burger
    success_url = reverse_lazy("burgers")
    pk_url_kwarg = "pk"
    template_name = "burger/burger_delete.html"
    context_object_name = "burger"

    def delete(self, request, *args, **kwargs):
        messages.error(request, "Burger was deleted successfully!")
        return super().delete(request, *args, **kwargs)



