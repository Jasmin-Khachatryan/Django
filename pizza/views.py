from helpers.decorators import own_restaurant_product
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from pizza.models import Pizza
from pizza.forms import PizzaForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class PizzaListView(ListView):
    model = Pizza
    template_name = "pizza/all_pizza.html"
    context_object_name = "pizzas"
    paginate_by = 2



class AboutUsView(TemplateView):
    template_name = "pizza/about_us.html"


class PizzaDetailView(DetailView):
    template_name = "pizza/pizza_info.html"
    price_range = 30
    calories_range = 40

    def get(self, request, pk):
        reference_pizza = get_object_or_404(Pizza, pk=pk)

        similar_pizzas = Pizza.objects.filter(
            Q(price__range=(reference_pizza.price - self.price_range, reference_pizza.price + self.price_range)) |
            Q(calories__range=(
            reference_pizza.calories - self.calories_range, reference_pizza.calories + self.calories_range))
        ).exclude(id=pk)

        context = {

            "pizzas": reference_pizza,
            "all_pizza": similar_pizzas,
        }

        return render(request, self.template_name, context)


class PizzaCreateView(CreateView):
    form_class = PizzaForm
    template_name = "pizza/add_pizza.html"
    context_object_name = "form"
    success_url = reverse_lazy("pizzas")

    def form_valid(self, form):

        form.save(commit=True)
        messages.success(self.request, "Pizza was created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pizzas")


class UpdatePizzaView(UpdateView):
    model = Pizza
    form_class = PizzaForm
    template_name = "pizza/update_pizza.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        form.save(commit=True)
        messages.info(self.request, "Pizza was updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pizza_info", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Pizza.objects.all()


class DeletePizzaView(DeleteView):
    model = Pizza
    template_name = "pizza/delete_pizza.html"
    context_object_name = "pizza"
    success_url = reverse_lazy("pizzas")
    pk_url_kwarg = "pk"

    def delete(self, request, *args, **kwargs):
        messages.error(request, "pizza was deleted successfully!")
        return super().delete(request, *args, **kwargs)




