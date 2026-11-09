class Employee:
  """Merepresentasikan data seorang karyawan."""

  def __init__(self, first_name, last_name, salary):
    self.first_name = first_name.title()
    self.last_name = last_name.title()
    self.salary = salary

  def give_raise(self, amount=5000):
    """Memberikan kenaikan gaji (default $5000 atau kustom)."""
    self.salary += amount