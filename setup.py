
from setuptools import setup, find_packages

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'name': 'MyPythonLibrary',
  'version': '0.1',
  'test_suite': 'tests',
}

setup(**config)

