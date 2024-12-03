class MealType:
    def __init__(self, name: str, calories: int, ingredients: List[str]):
        self.name = name
        self.calories = calories
        self.ingredients = ingredients

class MealTypeFactory:
    _meal_types = {}

    @classmethod
    def get_meal_type(cls, name: str, calories: int, ingredients: List[str]):
        key = (name, calories, tuple(ingredients))
        if key not in cls._meal_types:
            cls._meal_types[key] = MealType(name, calories, ingredients)
        return cls._meal_types[key]

class DailyMenu:
    def __init__(self):
        self.meals = []

    def add_meal(self, name: str, calories: int, ingredients: List[str]):
        meal_type = MealTypeFactory.get_meal_type(name, calories, ingredients)
        self.meals.append(meal_type)