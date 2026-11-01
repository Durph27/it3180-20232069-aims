import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartTest(unittest.TestCase):
    def test_cart_accepts_twenty_dvds_and_rejects_the_next_one(self):
        cart = Cart()

        for number in range(20):
            self.assertTrue(
                cart.add_dvd(DigitalVideoDisc(f"DVD {number}"))
            )

        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), 20)