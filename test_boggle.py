# import unittest

# To use unittest we have to create a class. This is specific to using unittest, so you may not have seen this code before.

# class TestBoggle(unittest.TestCase): # In other words, unittest tests if something inherits from. # IMPORTANT - case sensitive. 
    
    # def test_is_this_thing_on(self): 
        # When you create a class and you want to pass in methods to the class you use "self". This allows us to inherit from TestCase which includes all we need to run methods like assertEqual - which would have been undefined if we did not inlcude this.
        
        # self.assertEqual(1, 1) 
        # Now type "python3 -m unittest" into terminal to run test. # "-m" tells python3 that there is a "module" in the file called "unittest"


# Now to use the above with "boggle.py"

import unittest
from boggle import *
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    
    # def test_is_this_thing_on(self):
    #     answer = add(5, 3) # If we had simply used "import boggle" above we would have to use the "boggle." convention for all functions called. However, as we changed to "from boggle import *" we don't have to use it.
    #     self.assertEqual(answer, 8)
    # I have commented this out in "boggle.py" as we no longer need it.
        
    def test_empty_grid(self):
        grid = make_grid(0, 0)
        self.assertEqual(grid, {})
    
    def test_non_empty_grid(self):
        grid = make_grid(2, 2)
        self.assertEqual(len(grid), 4)
        
    def test_grid_has_upper_case_letters(self):
        grid = make_grid(2, 2)
        for c in grid.values():
            self.assertIn(c, ascii_uppercase)