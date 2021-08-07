class Garden:
    @staticmethod
    def _get_plants_abbr_dict() -> dict[str, str]:
        """Return dictionary: Name of the plant by its abbreviation."""

        plants = ("Grass", "Clover", "Radishes", "Violets")

        plant_by_abbr = {}
        for plant in plants:
            abbr = plant[0]
            plant_by_abbr[abbr] = plant
        return plant_by_abbr

    @staticmethod
    def _get_in_row_cup_slices_dict(students) -> dict[str, slice]:
        """Return dictionary: slice of the student's cups in each row by the name of the student"""

        in_row_cups_slice_by_student = {}
        slice_len = 2
        cur_slice_start = 0
        for student in sorted(students):
            in_row_cups_slice_by_student[student] = slice(
                cur_slice_start, cur_slice_start + slice_len
            )
            cur_slice_start += slice_len

        return in_row_cups_slice_by_student

    # Dict: name of the plant by its abbreviation
    # (which is a first letter of the plant)
    _plant_by_abbr = _get_plants_abbr_dict.__func__()

    _DEFAULT_STUDENTS = (
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    )

    def __init__(self, garden_diagram: str, students=_DEFAULT_STUDENTS):
        self._rows = self._parse_garden_diagram(garden_diagram)
        self._in_row_cups_slice_by_student = self._get_in_row_cup_slices_dict(students)

    @staticmethod
    def _parse_garden_diagram(diagram: str) -> list[str]:
        return diagram.splitlines()

    def plants(self, student: str) -> list[str]:
        plants = []
        cups_slice = self._in_row_cups_slice_by_student[student]
        for row in self._rows:
            plants += map(Garden._plant_by_abbr.get, row[cups_slice])
        return plants
