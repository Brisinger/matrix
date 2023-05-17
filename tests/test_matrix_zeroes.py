"""
Testing no. of contiguous zeroes in matrix.
"""
import unittest
from unittest import TestCase
from src.matrix_zeroes import zeroes_count


class TestMatrixZeroes(TestCase):
    """
    Test Class to unit test matrix_zeroes module.
    """

    def setUp(self) -> None:
        """
        Initial setup for testing
        """
        self.input = [[0, 2, 3, 0],
                      [0, 1, 0, 2],
                      [2, 1, 0, 2],
                      [0, 2, 1, 0]
                      ]
        self.expected = [2, 4, 1]
        return super().setUp()

    def test_matrix_zeroes(self) -> None:
        """
        Testing no. of contiguous zeroes in matrix.
        """
        # Arrange
        _input = self.input
        # Act
        result = zeroes_count(_input)
        # Assert
        self.assertEqual(self.expected, result)


if __name__ == "__main__":
    unittest.main()
