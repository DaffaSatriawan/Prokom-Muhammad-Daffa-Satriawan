import unittest
from Bab11_Lat03Function import Employee


class TestEmployee(unittest.TestCase):
  """Pengujian untuk kelas Employee."""

  def setUp(self):
    """Membuat objek employee yang bisa digunakan bersama oleh test method."""
    self.my_employee = Employee('muhammad', 'daffa', 60_000)

  def test_give_default_raise(self):
    """Menguji apakah kenaikan gaji default ($5000) bekerja dengan benar."""
    self.my_employee.give_raise()
    self.assertEqual(self.my_employee.salary, 65_000)

  def test_give_custom_raise(self):
    """Menguji apakah kenaikan gaji kustom (misal $10000) bekerja dengan benar."""
    self.my_employee.give_raise(10_000)
    self.assertEqual(self.my_employee.salary, 70_000)


if __name__ == '__main__':
  unittest.main()