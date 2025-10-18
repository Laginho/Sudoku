"""Tested functions

- has_nonzero_duplicate
- count_zeroes
- is_valid_input
- parse_puzzle_string
"""

import unittest

from utils import (
    has_nonzero_duplicate,
    count_zeroes,
    is_valid_input,
    parse_puzzle_string,
    EXAMPLE_BOARD,
)


class TestUtils(unittest.TestCase):

    def test_has_nonzero_duplicate(self) -> None:
        test_cases: list[tuple[list[int], bool, str]] = [
            (
                [1, 2, 3, 1],
                True,
                "Should detect duplicate non-zero numbers",
            ),
            (
                [1, 2, 3, 4],
                False,
                "Should not find duplicates where there are none",
            ),
            (
                [0, 1, 0, 2],
                False,
                "Should ignore duplicate zeroes",
            ),
            (
                [0, 0, 3, 4, 5, 0, 3, 2, 1, 0, 0],
                True,
                "Should handle complex cases with zeroes and duplicates",
            ),
            (
                [],
                False,
                "Should handle empty lists",
            ),
            (
                [5],
                False,
                "Should handle single-element lists",
            ),
            (
                [0, 0, 0],
                False,
                "Should return false for a list of only zeroes",
            ),
        ]

        for vector, expected, description in test_cases:
            with self.subTest(msg=description, vector=vector):
                self.assertEqual(has_nonzero_duplicate(vector), expected)

    def test_count_zeroes(self) -> None:
        board_no_zeroes: list[list[int]] = [[1] * 9 for _ in range(9)]
        board_all_zeroes: list[list[int]] = [[0] * 9 for _ in range(9)]

        test_cases: list[tuple[list[list[int]], int, str]] = [
            (
                EXAMPLE_BOARD,
                2,
                "Should correctly count zeroes in the example board",
            ),
            (
                board_no_zeroes,
                0,
                "Should return 0 for a board with no zeroes",
            ),
            (
                board_all_zeroes,
                81,
                "Should correctly count all cells if they are zeroes",
            ),
        ]

        for state, expected, description in test_cases:
            with self.subTest(msg=description):
                self.assertEqual(count_zeroes(state), expected)

    def test_is_valid_input(self) -> None:
        test_cases: list[tuple[list[str], bool, str]] = [
            (
                ["1", "2", "3"],
                True,
                "Should accept valid input",
            ),
            (
                ["9", "9", "9"],
                True,
                "Should accept boundary values (9)",
            ),
            (
                ["1", "1", "1"],
                True,
                "Should accept boundary values (1)",
            ),
            (
                ["1", "2"],
                False,
                "Should reject input with incorrect length (too short)",
            ),
            (
                ["1", "2", "3", "4"],
                False,
                "Should reject input with incorrect length (too long)",
            ),
            (
                ["a", "2", "3"],
                False,
                "Should reject input with non-digit characters",
            ),
            (
                ["1", "0", "3"],
                False,
                "Should reject input with numbers out of range (0)",
            ),
            (
                ["1", "10", "3"],
                False,
                "Should reject input with numbers out of range (10)",
            ),
            (
                ["1.0", "2", "3"],
                False,
                "Should reject non-integer strings",
            ),
        ]

        for entry, expected, description in test_cases:
            with self.subTest(msg=description, entry=entry):
                self.assertEqual(is_valid_input(entry), expected)

    def test_parse_puzzle_string(self) -> None:
        valid_string: str = "123456789" * 9
        parsed_valid_board: list[list[int]] = [
            [int(c) for c in "123456789"] for _ in range(9)
        ]

        test_cases: list[tuple[str, list[list[int]], str]] = [
            (
                valid_string,
                parsed_valid_board,
                "Should correctly parse a valid 81-digit string",
            ),
            (
                "0" * 81,
                [[0] * 9 for _ in range(9)],
                "Should correctly parse a string of all zeroes",
            ),
            (
                "1" * 80,
                [[]],
                "Should return empty list for string of "
                "incorrect length (too short)",
            ),
            (
                "1" * 82,
                [[]],
                "Should return empty list for string of incorrect length (too long)",
            ),
            (
                "a" * 81,
                [[]],
                "Should return empty list for string with non-digits",
            ),
            (
                "",
                [[]],
                "Should return empty list for an empty string",
            ),
        ]

        for puzzle_str, expected, description in test_cases:
            with self.subTest(msg=description):
                self.assertEqual(parse_puzzle_string(puzzle_str), expected)


if __name__ == "__main__":
    unittest.main()
