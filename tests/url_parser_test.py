
import unittest
from  src.url_parser import parse_url, get_domain

class UrlParserTest(unittest.TestCase):
  def setUp(self):
    pass
  def test1(self):
    self.assertEqual(parse_url("http://google.com")[0], "http")
  def test2(self):
    self.assertEqual(parse_url("http://google.com/fro")[1], "google.com")
  def test3(self):
    self.assertEqual(parse_url("http://google.com/oaefae")[2], None)
  def test4(self):
    self.assertEqual(parse_url("http://google.com/oaefae")[3], "/oaefae")
  def test5(self):
    with self.assertRaises(TypeError):
      parse_url(None)
  def test6(self):
    self.assertEqual(get_domain("http://google.com/fa"), "google.com")



