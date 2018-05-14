import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_none_price(self):
        self.assertIsNone(format_price())

    def test_minus_price(self):
        self.assertEqual('-4', format_price(-4.0))
        self.assertEqual('-5.50', format_price(-5.5000))

    def test_zero_num_price(self):
        self.assertEqual('0.50', format_price(.5))
        self.assertEqual('0.10', format_price(.099))

    def test_str_price(self):
        self.assertEqual(None, format_price('qwe'))


if __name__ == '__main__':
    unittest.main()
