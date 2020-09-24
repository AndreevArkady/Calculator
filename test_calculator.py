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
        self.assertAlmostEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_mul(self):
        self.calculator.value = random.random() * 100
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        self.calculator.value = random.random() * 100
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_power(self):
        times = time.time()
        local_time = time.gmtime(times)
        print("Power test start time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")
        self.calculator = Calculator(random.random() * 100)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.power(1.3, 3.7).value, calc_value ** (1.3 * 3.7))
        times = time.time()
        local_time = time.gmtime(times)
        print("Power test end time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")

    def test_root(self):
        times = time.time()
        local_time = time.gmtime(times)
        print("Root test start time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")
        self.calculator = Calculator(random.random() * 100)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.root(1.9 * 4.5).value, calc_value ** (1 / (1.9 * 4.5)))
        times = time.time()
        local_time = time.gmtime(times)
        print("Root test end time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")

    def test_root_divide_substract(self):
        times = time.time()
        local_time = time.gmtime(times)
        print("root_divide_substract test start time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")
        self.calculator = Calculator(random.random() * 1000000)
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2, 3).divide(5, 3.2).subtract(228, 666).value,
                         (calc_value ** (1/6)) / (5 * 3.2) - 228 - 666)
        times = time.time()
        local_time = time.gmtime(times)
        print("root_divide_substract test end time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")

    def test_multi_power_add(self):
        times = time.time()
        local_time = time.gmtime(times)
        print("test_multi_power_add test start time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")
        self.calculator = Calculator(random.random() * 100)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.multiply(1.2, 3.4).power(2, 1.3).add(13, 19).value,
                               (calc_value * 1.2 * 3.4) ** (2 * 1.3) + (13 + 19))
        Calculator(3).add().multiply()
        local_time = time.gmtime(times)
        print("test_multi_power_add test end time: ", (local_time.tm_hour + 3) % 24,
              ':', local_time.tm_min, ':', local_time.tm_sec, '.',
              "%6d" % ((times % 1) * 1000000), sep="")

if __name__ == '__main__':
    unittest.main()
