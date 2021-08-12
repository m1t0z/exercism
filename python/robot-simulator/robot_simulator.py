# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

_DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
_CNT_DIRECTIONS = len(_DIRECTIONS)


class Robot:
    def __init__(self, direction: int = NORTH, x: int = 0, y: int = 0):

        if direction not in _DIRECTIONS:
            raise ValueError("Unknow direction '{direction}'!")

        self._x = x
        self._y = y
        self._dir = direction
        pass

    @property
    def coordinates(self) -> tuple[int, int]:
        return (self._x, self._y)

    @property
    def direction(self) -> int:
        return self._dir

    def move(self, movements: str):
        for movement in movements:
            self._make_movement(movement)

    def _make_movement(self, movement: str):
        if movement == "L":
            self._turn_left()
        elif movement == "R":
            self._turn_right()
        elif movement == "A":
            self._advance()
        else:
            raise ValueError(f"Unknown movement '{movement}'!")

    def _turn_right(self):
        self._dir = (self._dir + 1) % _CNT_DIRECTIONS

    def _turn_left(self):
        self._dir = (self._dir - 1) % _CNT_DIRECTIONS

    def _advance(self):
        if self._dir == NORTH:
            self._y += 1
        elif self._dir == EAST:
            self._x += 1
        elif self._dir == SOUTH:
            self._y -= 1
        elif self._dir == WEST:
            self._x -= 1
        else:
            assert False
