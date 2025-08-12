def add_ingredients_to_constructor(constructor_page, ingredient_indices):
    for index in ingredient_indices:
        constructor_page.drag_and_drop_ingredient_by_counter(index)

