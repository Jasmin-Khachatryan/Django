from django import forms
from django.forms import TextInput, Textarea, NumberInput, ClearableFileInput, Select
from burgers.models import Burger
from restaurant.models import Restaurant


class BurgerForm(forms.ModelForm):
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all())

    class Meta:

        widgets ={

            "burger_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title",
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description",
                "rows": 2,
                "cols": 2
            }),
            "rate": NumberInput(attrs={
                "class": "form-control",
                "size": 5
            }),
            "prepare_time": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Prepare time",
                "size": 5
            }),
            "calories":NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Calories",
                "size": 5
            }),
            "price": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Calories",
                "size": 5
            }),
            "image": ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*"
            }),
            'restaurant': Select(attrs={
                "class": "form-control"
            })
 }

        model = Burger
        fields = ("burger_name", "description", "rate", "prepare_time",
                  "calories", "price", "image", "restaurant")

