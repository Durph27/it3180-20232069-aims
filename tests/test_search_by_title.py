import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchByTitleTest(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
            DigitalVideoDisc("Aladdin"),
        ]

    def test_search_by_title_matches_partially_and_ignores_case(self):
        result = search_by_title("LION", self.dvds)

        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])

    def test_search_by_title_preserves_original_order(self):
        result = search_by_title("a", self.dvds)

        self.assertEqual(
            [dvd.title for dvd in result],
            ["Star Wars", "Aladdin"],
        )

    def test_search_by_title_returns_empty_list_when_not_found(self):
        self.assertEqual(search_by_title("Comedy", self.dvds), [])


if __name__ == "__main__":
    unittest.main()