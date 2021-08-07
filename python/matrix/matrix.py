class Matrix:
    def __init__(self, matrix: str):
        self._matrix = Matrix._parse_matrix(matrix)

    def row(self, number: int) -> list[int]:
        return self._matrix[number - 1]

    def column(self, number: int) -> list[int]:
        return [row[number - 1] for row in self._matrix]

    @staticmethod
    def _parse_matrix(matrix: str) -> list[list[int]]:
        parsed = []
        for row in matrix.splitlines():
            parsed.append(Matrix._parse_row(row))
        return parsed

    @staticmethod
    def _parse_row(row: str) -> list[int]:
        return [int(token) for token in row.split()]
