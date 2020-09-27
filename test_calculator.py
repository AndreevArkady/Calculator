import unittest
import time
import random
from simple_calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(1)

    def test_add(self):
        self.calculator.value = random.random() * 100
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.add(1, 22, 3, 0).value, calc_value + 26)

    def test_mul(self):
        self.calculator.value = random.random() * 100
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        self.calculator.value = random.random() * 100
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.divide(5, 3, 1, 7).value, calc_value / 105)

    def test_subtract(self):
        self.calculator.value = random.random() * 100
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.subtract(8, 10, 37).value, calc_value - 55)

    def test_power(self):
        get_start_time("power")
        self.calculator = Calculator(random.random() * 100)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.power(1.3, 3.7).value, calc_value ** (1.3 * 3.7))
        get_end_time("power")

    def test_root(self):
        get_start_time("root")
        self.calculator = Calculator(random.random() * 100)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.root(1.9 * 4.5).value, calc_value ** (1 / (1.9 * 4.5)))
        get_end_time("root")

    def test_root_divide_subtract(self):
        get_start_time("root_divide_subtract")
        self.calculator = Calculator(random.random() * 1000000)
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2, 3).divide(5, 3.2).subtract(228, 666).value,
                         (calc_value ** (1 / 6)) / (5 * 3.2) - 228 - 666)
        get_end_time("root_divide_subtract")

    def test_multi_power_add(self):
        get_start_time("multi_power_add")
        self.calculator = Calculator(random.random() * 100)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.multiply(1.2, 3.4).power(2, 1.3).add(13, 19).value,
                               (calc_value * 1.2 * 3.4) ** (2 * 1.3) + (13 + 19))
        Calculator(3).add().multiply()
        get_end_time("multi_power_add")


def get_start_time(s):
    times = time.time()
    local_time = time.gmtime(times)
    print(s, " test start time: ", (local_time.tm_hour + 3) % 24,
          ':', local_time.tm_min, ':', local_time.tm_sec, '.',
          "%8d" % ((times % 1) * 1e8), sep="")


def get_end_time(s):
    times = time.time()
    local_time = time.gmtime(times)
    print(s, " test end time: ", (local_time.tm_hour + 3) % 24,
          ':', local_time.tm_min, ':', local_time.tm_sec, '.',
          "%8d" % ((times % 1) * 1e8), sep="")


if __name__ == '__main__':
    unittest.main()
