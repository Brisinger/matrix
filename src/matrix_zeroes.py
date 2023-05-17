"""
This module finds the no. of zeroes contiguous in all eight directions 
"""


def zeroes_count(matrix: list[list[int]]) -> list[int]:
    """
    Counts the no. of contiguous zeroesby horizontally, vertically and diagonally.

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


if __name__ == "__main__":
    _input = [[0, 2, 3, 0],
              [0, 1, 0, 2],
              [2, 1, 0, 2],
              [0, 2, 1, 0]
              ]
    ans = zeroes_count(_input)
    print(ans)
