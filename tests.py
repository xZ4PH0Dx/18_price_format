import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_none_price(self):
        self.assertIsNone(format_price())

    def test_mutable_obj_price(self):
        self.assertIsNone(format_price([]))
        self.assertIsNone(format_price({}))

    def test_big_price(self):
        self.assertEqual('123 456 789', format_price(123456789.000))
        self.assertEqual('123 456 789.90', format_price(123456789.900))

    def test_minus_price(self):
        self.assertEqual('-4', format_price(-4.0))
        self.assertEqual('-5.50', format_price(-5.5000))

    def test_zero_num_price(self):
        self.assertEqual('0.50', format_price(.5))
        self.assertEqual('0.10', format_price(.099))

    def test_str_price(self):
        self.assertIsNone(format_price('qwe'))
        self.assertIsNone(format_price('123/45'))

    def test_bool_price(self):
        self.assertIsNone(format_price(True))
        self.assertIsNone(format_price(False))


if __name__ == '__main__':
    unittest.main()
