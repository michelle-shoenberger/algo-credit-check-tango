from credit_check import credit_check
import unittest

class CreditTester(unittest.TestCase):

    valid_numbers =  "5541808923795240"
    invalid_numbers = "5541801923795240"
    simple_numbers = "129"

    def test_return(self):
        """ This tests that function returns a value"""
        self.assertIsNotNone(credit_check(self.valid_numbers))

    # def test_change_input(self):
    #     """Tests the input is changed to array"""
    #     self.assertEqual(credit_check(self.simple_numbers), [1,2,3])

    # def test_every_other_input(self):
    #     """Tests the program doubles every other digit"""
    #     self.assertEqual(credit_check(self.simple_numbers), [2,2,6])

    # def test_sum(self):
    #     """Tests the program sums digits over 10"""
    #     self.assertEqual(credit_check(self.simple_numbers), [2,2,9])

    # def test_modulo(self):
    #     """Tests the program sums all and returns modulo of 10"""
    #     self.assertEqual(credit_check(self.simple_numbers), 3)

    def test_valid(self):
        """Tests the program returns valid on the right input"""
        self.assertEqual(credit_check(self.valid_numbers), "The number is valid!")

    def test_invalid(self):
        """Tests the program returns valid on the right input"""
        self.assertEqual(credit_check(self.invalid_numbers), "The number is invalid!")


if __name__ == "__main__":
    unittest.main()




# print(credit_check('5541808923795240') == "The number is valid!")
# print(credit_check("4024007136512380") == "The number is valid!")
# print(credit_check("6011797668867828") == "The number is valid!")

# print(credit_check("5541801923795240") == "The number is invalid!")
# print(credit_check("4024007106512380") == "The number is invalid!")
# print(credit_check("6011797668868728") == "The number is invalid!")