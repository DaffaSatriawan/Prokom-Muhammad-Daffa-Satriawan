import unittest
from Bab11_Lat01Function import city_country


class CitiesTestCase(unittest.TestCase):
  """Pengujian untuk city_functions.py"""

  def test_city_country(self):
    """Apakah kota seperti 'santiago' dan 'chile' berfungsi dengan benar?"""
    formatted_name = city_country("santiago", "chile")
    self.assertEqual(formatted_name, "Santiago, Chile")


if __name__ == "__main__":
  unittest.main()