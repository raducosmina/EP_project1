from unittest import TestCase
from main import median
from main import media_aritmetica
from main import domeniu_dispersie
from main import deviatia
from main import coef_variatie


class Test(TestCase):
    persoane = [40, 43, 34, 44, 52, 51, 63, 36, 54, 43, 67, 45, 55, 57, 48, 45, 71, 51, 54, 47, 39, 50, 26, 62, 33, 40,
                42, 55, 29, 45]

    def test_median(self):
        self.assertEqual(median(self.persoane), 47)

    def test_media_aritmetica(self):
        self.assertAlmostEqual(media_aritmetica(self.persoane), 47.3666666666666)

    def test_domeniu_dispersie(self):
        self.assertEqual(domeniu_dispersie(self.persoane), None)

    def test_deviatia(self):
        self.assertEqual(deviatia(self.persoane), 10.54666877370396)

    def test_coef_variatie(self):
        self.assertAlmostEqual(coef_variatie(self.persoane), 0.22266014300571)
