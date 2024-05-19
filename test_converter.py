import unittest
from proekt import convert_temperature

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert_temperature(0, "Цельсий", "Фаренгейт"), 32.00)
        self.assertEqual(convert_temperature(100, "Цельсий", "Фаренгейт"), 212.00)

    def test_celsius_to_kelvin(self):
        self.assertEqual(convert_temperature(0, "Цельсий", "Кельвин"), 273.15)
        self.assertEqual(convert_temperature(100, "Цельсий", "Кельвин"), 373.15)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert_temperature(32, "Фаренгейт", "Цельсий"), 0.00)
        self.assertEqual(convert_temperature(212, "Фаренгейт", "Цельсий"), 100.00)

    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(convert_temperature(32, "Фаренгейт", "Кельвин"), 273.15)
        self.assertEqual(convert_temperature(212, "Фаренгейт", "Кельвин"), 373.15)

    def test_kelvin_to_celsius(self):
        self.assertEqual(convert_temperature(273.15, "Кельвин", "Цельсий"), 0.00)
        self.assertEqual(convert_temperature(373.15, "Кельвин", "Цельсий"), 100.00)

    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(convert_temperature(273.15, "Кельвин", "Фаренгейт"), 32.00)
        self.assertEqual(convert_temperature(373.15, "Кельвин", "Фаренгейт"), 212.00)

    def test_same_unit(self):
        self.assertEqual(convert_temperature(10, "Цельсий", "Цельсий"), 10.00)

if __name__ == '__main__':
    unittest.main()
