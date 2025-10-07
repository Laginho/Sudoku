import unittest

from utils import has_nonzero_duplicate


class TestUtils(unittest.TestCase):

    def test_has_nonzero_duplicate(self):
        # Case 1: A list with no duplicates
        no_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertFalse(
            has_nonzero_duplicate(no_duplicates),
            "Should be False for a list with no duplicates",
        )

        # Case 2: A list with duplicates
        with_duplicates = [1, 2, 3, 4, 5, 1, 7, 8, 9]
        self.assertTrue(
            has_nonzero_duplicate(with_duplicates),
            "Should be True for a list with duplicates",
        )

        # Case 3: A list with zeroes and no other duplicates
        with_zeroes = [0, 1, 2, 3, 0, 4, 5, 6, 7]
        self.assertFalse(
            has_nonzero_duplicate(with_zeroes),
            "Should be False as zeroes are ignored",
        )

        # Case 4: A list with zeroes and other duplicates
        with_zeroes_and_duplicates = [0, 1, 2, 1, 0, 4, 5, 6, 7]
        self.assertTrue(
            has_nonzero_duplicate(with_zeroes_and_duplicates),
            "Should be True for duplicates even with zeroes present",
        )


if __name__ == "__main__":
    unittest.main()
