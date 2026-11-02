import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items = [
            DigitalVideoDisc("The Lion King", cost=19.95),
            DigitalVideoDisc("aladdin", cost=18.99),
            DigitalVideoDisc("Star Wars", cost=24.95),
        ]

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in self.cart.items],
            ["aladdin", "Star Wars", "The Lion King"],
        )

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in self.cart.items],
            [18.99, 19.95, 24.95],
        )


if __name__ == "__main__":
    unittest.main()