from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipes_view(request, dish_name):
    """Отображение списка ингридиентов для блюда с поддержкой расчёта количества порций

    :param request: данные вызова
    :param dish_name: название блюда
    """

    ingredients = DATA.get(dish_name)
    if request.GET.get('servings'):
        ingredients = _servings(ingredients, float(request.GET.get('servings')))
    context = {'recipe': ingredients}

    return render(request, 'calculator/index.html', context)


def _servings(ingredients: dict, amount: float):
    """Пересчёт количества ингредиентов в зависимости от порций

    :param ingredients: ингредиены блюда
    :param amount: количество порций (параметр servings из request)
    """

    update_ingredients = dict()
    for product, product_amount in ingredients.items():
        update_ingredients[product] = product_amount * amount

    return update_ingredients
