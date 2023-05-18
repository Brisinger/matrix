"""
Testing no. of contiguous zeroes in matrix.
"""
import unittest
from unittest import TestCase
from src.matrix_zeroes import zeroes_count, count_zeroes


class TestMatrixZeroes(TestCase):
    """
    Test Class to unit test matrix_zeroes module.
    """

    def setUp(self) -> None:
        """
        Initial setup for testing
        """
        self.input1 = [[0, 2, 3, 1],
                       [0, 1, 0, 2],
                       [2, 1, 0, 2],
                       [0, 2, 1, 0]
                       ]
        self.input2 = [[0, 2, 3, 1],
                       [0, 1, 0, 0],
                       [2, 0, 0, 2],
                       [0, 2, 1, 0]
                       ]
        self.expected1 = [2, 3, 1]
        self.expected2 = [8]
        return super().setUp()

    def test_matrix_zeroes(self) -> None:
        """
        Testing no. of contiguous zeroes in matrix.
        """
        # Arrange
        _input1 = self.input1
        _input2 = self.input2
        # Act
        result1 = zeroes_count(_input1)
        result2 = count_zeroes(_input2)
        # Assert
        self.assertEqual(self.expected1, result1)
        self.assertEqual(self.expected2, result2)


if __name__ == "__main__":
    unittest.main()
