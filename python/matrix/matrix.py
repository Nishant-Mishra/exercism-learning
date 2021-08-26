class Matrix:
    def __init__(self, matrix_string: str):
        lines = matrix_string.split('\n')
        self._nums = [list(map(int, line.split())) for line in lines]
        self._colsz = len(self._nums[0])
        self._rowsz = len(self._nums)
        self._elems = self._rowsz * self._colsz

    def row(self, index: int):
        if index > self._rowsz:
            raise ValueError(f"Invalid index '{index}'")
        return self._nums[index - 1]

    def column(self, index: int):
        if index > self._colsz:
            raise ValueError(f"Invalid index '{index}'")
        return [self._nums[i][index - 1] for i in range(self._rowsz)]
