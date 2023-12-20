# forms.py
from django import forms
from restaurant.models import Restaurant
from django.forms import inlineformset_factory
from pizza.models import Pizza
from burgers.models import Burger
from pizza.forms import PizzaForm
from burgers.forms import BurgerForm

RestaurantPizzaFormSet = inlineformset_factory(Restaurant, Pizza, form=PizzaForm, extra=2, can_delete=False)
RestaurantBurgerFormSet = inlineformset_factory(Restaurant, Burger, form=BurgerForm, extra=2, can_delete=False)


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'description', 'date', 'image']

