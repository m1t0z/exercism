import collections


class School:
    def __init__(self):
        self._students_by_grade = collections.defaultdict(list)

    def add_student(self, name: str, grade: int) -> None:
        self._students_by_grade[grade].append(name)

    def roster(self) -> list[str]:
        roster = []
        for grade in sorted(self._students_by_grade):
            roster += sorted(self._students_by_grade[grade])
        return roster

    def grade(self, grade: int) -> list[str]:
        return sorted(self._students_by_grade[grade])
