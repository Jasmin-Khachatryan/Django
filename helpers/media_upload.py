def upload_pizza_image(instance, filename):
    return f"pizzas/{instance.pizza_name}/{filename}"

def upload_burger_image(instance, filename):
    return f"burgers/{instance.burger_name}/{filename}"


def upload_restaurant_image(instance, filename):
    return f"restaurant/{instance.restaurant_name}/{filename}"