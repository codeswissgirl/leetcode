import unittest
from typing import List

def letterCombinations(digits):
    res=[] #end we want to have a list of strings
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'qprs',
        '8':'tuv',
        '9':'wxyz',
    }
    #recursive call to get all combinations: a, abc, def def def, how many times: 4^n wheres n is the lenght of digits
    def backtrack(i, path): #i stands for index, such as 012 012, path: is a string 
        #basecase that function stops
        if len(path)==len(digits):
            res.append(path) #idk 
        #recursive call
        for c in mapping[digits[index]]: #c stands for each character such as a, b, c
            backtrack(i+1, path+c)
    backtrack(0,'')
  return res

#Unit test
class TestLetterCombinations(unittest.TestCase):
    def test_example_1(self):
        digits = "23"
        expected_result = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertCountEqual(letterCombinations(digits), expected_result)

    def test_example_2(self):
        digits = ""
        expected_result = []
        self.assertEqual(letterCombinations(digits), expected_result)

    def test_example_3(self):
        digits = "2"
        expected_result = ["a","b","c"]
        self.assertCountEqual(letterCombinations(digits), expected_result)


# run the unit tests
if __name__ == '__main__':
    unittest.main()
