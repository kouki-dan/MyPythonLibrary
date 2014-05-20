
import unittest
from  src.base_str import base_str

class BaseStrTest(unittest.TestCase):
  def setUp(self):
    pass
  def test1(self):
    self.assertEqual(base_str(10,10), "10")
  def test2(self):
    self.assertEqual(base_str(10,60), "a")
  def test3(self):
    self.assertEqual(base_str(1351,62), "lN")
  def test4(self):
    with self.assertRaises(ValueError):
      base_str(60,63)
  def test5(self):
    self.assertEqual(base_str(-1351,62), "-lN")
