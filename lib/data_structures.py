spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return([spicy_food["name"] for spicy_food in spicy_foods])


def get_spiciest_foods(spicy_foods):
    return([spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5])

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print("{food_name} {cuisine}: Heat Level: {heat_indicator}"
              .format(food_name = spicy_food["name"], cuisine = spicy_food["cuisine"], heat_indicator = "🌶"*spicy_food["heat_level"]))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass

print (get_names(spicy_foods))
print (get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)