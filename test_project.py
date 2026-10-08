import unittest
import validator
class ProjectTests(unittest.TestCase):
    def test_empty_string(self):
     self.assertFalse9validator.check_text("   ")
    def test_good_string(self):
        self.assertEqual(validator.check_text(" Study Python "), "Study Python")
    def test_bad_number(self):
       self.assertFalse(validator.check_number("10, 3"))
if __name__ == "__main__":
    unittest.main()
