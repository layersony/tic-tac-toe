#! /usr/bin/python3


import unittest
from unittest.main import TestProgram
import run

class Test_tic(unittest.TestCase):

  def test_checkwin(self):
    trial1 = [1,4,7]
    trial2 = [3,5,2,7]
    trial3 = [7,8,9]
    trial4 = [2,5,3]
    trial5 = [6,5,8]


    result = run.checkwin(trial1)
    result2 = run.checkwin(trial2)
    result3 = run.checkwin(trial3)
    result4 = run.checkwin(trial4)
    result5 = run.checkwin(trial5)

    self.assertEqual(result, True)
    self.assertEqual(result2, False)
    self.assertEqual(result3, True)
    self.assertEqual(result4, False)
    self.assertEqual(result5, False)
    
  def test_redo(self):
      trial = 'y'
      trial2 = "Y"
      trial3 = "n"
      trial4 = 4

      result = run.retake()

      self.assertEqual(result, 'y')
      self.assertEqual(result, 'n')



if __name__ == "__main__":
  unittest.main()
