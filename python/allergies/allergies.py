_ALLERGENS = (
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
)


def _get_allergens(score: int) -> list[str]:
    _allergens = []
    for i, allergen in enumerate(_ALLERGENS):
        bit_n = 1 << i
        if score & bit_n:
            _allergens.append(allergen)
    return _allergens


class Allergies:
    def __init__(self, score: int):
        self._allergens = _get_allergens(score)

    def allergic_to(self, item: str) -> bool:
        return item in self._allergens

    @property
    def lst(self) -> list[str]:
        return self._allergens
