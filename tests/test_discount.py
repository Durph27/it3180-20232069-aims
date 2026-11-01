import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("DVD", cost=100))

    def test_no_discount(self):
        self.assertEqual(self.cart.total_cost(0), 100)

    def test_ten_percent_discount(self):
        self.assertEqual(self.cart.total_cost(10), 90)

    def test_full_discount(self):
        self.assertEqual(self.cart.total_cost(100), 0)

    def test_discount_over_one_hundred_percent_raises_error(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost(101)