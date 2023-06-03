"""
This module finds the no. of zeroes contiguous in all eight directions 
"""


def zeroes_count(matrix: list[list[int]]) -> list[int]:
    """
    Counts the no. of contiguous zeroes visited horizontally, vertically and diagonally.

    Args:
    -----
        matrix (list:list[int]): Input square matrix.

    Returns:
    --------
        list[int]: List containing no. of contiguous zeroes in square matrix.
    """
    _n = len(matrix)
    memo = [[0] * _n for _ in range(_n)]
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1),
                  (-1, 1), (-1, -1), (1, -1), (1, 1))

    def dfs(row: int, col: int) -> int:
        if memo[row][col] != 0:
            return memo[row][col]
        matrix[row][col] = -1
        for point in directions:
            _x, _y = (point[0] + row), (point[1] + col)
            if 0 <= _x < _n and 0 <= _y < _n and matrix[_x][_y] == 0:
                memo[row][col] += dfs(_x, _y)
        memo[row][col] += 1
        return memo[row][col]

    result = []
    for row in range(_n):
        for col in range(_n):
            if matrix[row][col] != 0:
                continue
            count = dfs(row, col)
            result.append(count)
    return result


def count_zeroes(matrix: list[list[int]]) -> list[int]:
    """
    Counts the no. of contiguous zeroes by traversing horizontally, vertically and diagonally.
    It doesn't use additional memory for storing results of depth-first search.

    Args:
    -----
        matrix (list:list[int]): Input square matrix.

    Returns:
    --------
        list[int]: List containing no. of contiguous zeroes in square matrix.
    """
    _n = len(matrix)
    _directions = ((0, 1), (1, 0), (-1, 0), (0, -1),
                   (-1, 1), (-1, -1), (1, -1), (1, 1))

    def dfs(row, col, count=0) -> int:
        matrix[row][col] = -1
        for point in _directions:
            _x, _y = (point[0] + row), (point[1] + col)
            if 0 <= _x < _n and 0 <= _y < _n and matrix[_x][_y] == 0:
                count += dfs(_x, _y)
        return count + 1
    result = []
    for row in range(_n):
        for col in range(_n):
            if matrix[row][col] != 0:
                continue
            _ans = dfs(row, col)
            result.append(_ans)
    return result


def zeroes(matrix: list[list[int]]) -> list[int]:
    """
    Counts the no. of contiguous zeroes by traversing horizontally, vertically and diagonally.
    It doesn't use additional memory for storing results of depth-first search.
    Depth-First search uses two parameters returning the count of zeroes during unwinding phase.

    Args:
    -----
        matrix (list:list[int]): Input square matrix.

    Returns:
    --------
        list[int]: List containing no. of contiguous zeroes in square matrix.
    """
    _n = len(matrix)
    _directions = ((0, 1), (1, 0), (-1, 0), (0, -1),
                   (-1, 1), (-1, -1), (1, -1), (1, 1))
    result = []

    def dfs(row: int, col: int) -> int:
        """
        Performs depth-first search from a given row and column of square matrix.
        Move left, right, up , down and diagonally untill adjacent 0's are found.
        Change the value of cell in given row and column of matrix if 0 so that its not visited again.

        Args:
        -----
            row (int): Row index of input matrix.
            col (int): Column index of input matrix.

        Returns:
        --------
           int: No. of contiguous 0's from given row and column index of matrix
        """
        count = 0
        matrix[row][col] = -1
        for point in _directions:
            x, y = (point[0] + row), (point[1] + col)
            if 0 <= x < _n and 0 <= y < _n and matrix[x][y] == 0:
                count += dfs(x, y)
        return count + 1
    # Traverse the matrix to detect contiguous zeroes from each cell.
    for row in range(_n):
        for col in range(_n):
            count = 0
            if matrix[row][col] == 0:
                count = dfs(row, col)
                result.append(count)
    return result


if __name__ == "__main__":
    _input = [[0, 2, 3, 0],
              [0, 1, 0, 2],
              [2, 1, 0, 2],
              [0, 2, 1, 0]
              ]
    ans = zeroes_count(_input)
    print(ans)
    # Second alternative.
    _input = [[0, 2, 3, 0],
              [0, 1, 0, 2],
              [2, 1, 0, 2],
              [0, 2, 1, 0]
              ]
    ans = count_zeroes(_input)
    print(ans)
    _input = [[0, 2, 3, 0],
              [0, 1, 0, 0],
              [2, 1, 0, 2],
              [0, 2, 1, 0]
              ]
    ans = zeroes(_input)
    print(ans)
