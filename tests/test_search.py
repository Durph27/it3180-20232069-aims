import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Science Fiction"),
            DigitalVideoDisc("Aladdin", category="Animation"),
        ]

    def test_search_by_category_is_case_insensitive(self):
        result = search_by_category(self.dvds, "animation")

        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King", "Aladdin"],
        )

    def test_search_by_category_returns_empty_result_when_not_found(self):
        self.assertEqual(search_by_category(self.dvds, "Comedy"), [])

    def test_search_by_title_is_case_insensitive_and_matches_partial_title(self):
        result = search_by_title("LION", self.dvds)

        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])

    def test_search_by_title_preserves_dvd_order(self):
        result = search_by_title("a", self.dvds)

        self.assertEqual(
            [dvd.title for dvd in result],
            ["Star Wars", "Aladdin"],
        )


if __name__ == "__main__":
    unittest.main()