import unittest

# Mengimpor fungsi city_country dari file Bab11_Lat02Function
from Bab11_Lat02Function import city_country


class CitiesTestCase(unittest.TestCase):
  """Pengujian untuk city_functions dengan populasi."""

  def test_city_country(self):
    """Apakah kota seperti 'santiago' dan 'chile' berfungsi?"""
    formatted_name = city_country("santiago", "chile")
    self.assertEqual(formatted_name, "Santiago, Chile")

  def test_city_country_population(self):
    """Apakah kota dengan populasi berfungsi dengan benar?"""
    formatted_name = city_country("santiago", "chile", 5000000)
    self.assertEqual(formatted_name, "Santiago, Chile - population 5000000")


if __name__ == "__main__":
  unittest.main()