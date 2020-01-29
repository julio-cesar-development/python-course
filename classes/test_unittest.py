# -*- coding: utf-8 -*-
import unittest
import math

print(math.pow(2, 2))

print(math.sqrt(4))

class TestMathMethods(unittest.TestCase):
  def test_potency(self):
    self.assertEqual(4, math.pow(2, 2))

  def test_square(self):
    self.assertEqual(2, math.sqrt(4))

unittest.main()
