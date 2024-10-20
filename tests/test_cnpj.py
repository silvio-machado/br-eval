import unittest
from br_eval.cnpj import clean_cnpj, generate_cnpj, format_cnpj, validate_cnpj
from br_eval.exceptions.cnpj_exceptions import (
    InvalidCNPJError,
    RepeatedDigitsCNPJError,
    InvalidLengthCNPJError
)

class TestCNPJ(unittest.TestCase):
    def test_valid_cnpj(self):
        self.assertTrue(validate_cnpj("13.347.016/0001-17"))  # Example CNPJ
        self.assertTrue(validate_cnpj("00.000.000/0001-91"))
        self.assertTrue(validate_cnpj("00000000000191"))

    def test_valid_cnpj_generator(self):
        """
        This test will generate 10 valid CNPJs and check if they are valid.
        Also generates 10 formatted CNPJs and checks if they are valid.
        """
        for _ in range(10):
            cnpj = generate_cnpj()
            self.assertTrue(validate_cnpj(cnpj))
        for _ in range(10):
            cnpj = generate_cnpj(formatted=True)
            self.assertTrue(validate_cnpj(cnpj))
    
    def test_invalid_verification_digits(self):
        with self.assertRaises(InvalidCNPJError):
            validate_cnpj("13.347.016/0001-18")  # Altered last digit
    
    def test_repeated_digits_cnpj(self):
        with self.assertRaises(RepeatedDigitsCNPJError):
            validate_cnpj("11.111.111/1111-11")
        with self.assertRaises(RepeatedDigitsCNPJError):
            validate_cnpj("22222222222222")
    
    def test_invalid_characters_cnpj(self):
        with self.assertRaises(InvalidLengthCNPJError):
            validate_cnpj("13.347.016/0001-1A")
    
    def test_invalid_length_cnpj(self):
        with self.assertRaises(InvalidLengthCNPJError):
            validate_cnpj("13.347.016/0001-1")
        with self.assertRaises(InvalidLengthCNPJError):
            validate_cnpj("13.347.016/0001-177")
    
    def test_clean_cnpj(self):
        cnpj_clean = clean_cnpj("13.347.016/0001-17")
        self.assertEqual(cnpj_clean, "13347016000117")
    
    def test_format_cnpj(self):
        cnpj_formatted = format_cnpj("13347016000117")
        self.assertEqual(cnpj_formatted, "13.347.016/0001-17")
    
    def test_whitespace_cnpj(self):
        self.assertTrue(validate_cnpj(" 13.347.016/0001-17 "))
    
    def test_all_same_digits(self):
        with self.assertRaises(RepeatedDigitsCNPJError):
            validate_cnpj("00000000000000")
        with self.assertRaises(RepeatedDigitsCNPJError):
            validate_cnpj("99.999.999/9999-99")

if __name__ == '__main__':
    unittest.main()
