_EARH_ORBITAL_PERIOD_S = 31557600
_MERCURY_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 0.2408467
_VENUS_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 0.61519726
_MARS_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 1.8808158
_JUPITER_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 11.862615
_SATURN_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 29.447498
_URANUS_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 84.016846
_NEPTUNE_ORBITAL_PERIOS_S = _EARH_ORBITAL_PERIOD_S * 164.79132


class SpaceAge:
    def __init__(self, seconds: int):
        self._seconds = seconds
        pass

    def _to_years(self, orbital_perios_s: float) -> float:
        return round(self._seconds / orbital_perios_s, 2)

    def on_earth(self) -> float:
        return self._to_years(_EARH_ORBITAL_PERIOD_S)

    def on_mercury(self) -> float:
        return self._to_years(_MERCURY_ORBITAL_PERIOS_S)

    def on_venus(self) -> float:
        return self._to_years(_VENUS_ORBITAL_PERIOS_S)

    def on_mars(self) -> float:
        return self._to_years(_MARS_ORBITAL_PERIOS_S)

    def on_jupiter(self) -> float:
        return self._to_years(_JUPITER_ORBITAL_PERIOS_S)

    def on_saturn(self) -> float:
        return self._to_years(_SATURN_ORBITAL_PERIOS_S)

    def on_uranus(self) -> float:
        return self._to_years(_URANUS_ORBITAL_PERIOS_S)

    def on_neptune(self) -> float:
        return self._to_years(_NEPTUNE_ORBITAL_PERIOS_S)
