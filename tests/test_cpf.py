import unittest
from br_eval.cpf import format_cpf, clean_cpf, generate_cpf, validate_cpf
from br_eval.exceptions.cpf_exceptions import (
    InvalidCPFError,
    RepeatedDigitsCPFError,
    InvalidFormatCPFError,
    InvalidLengthCPFError,
)

class TestCPF(unittest.TestCase):
    def test_valid_cpf(self):
        self.assertTrue(validate_cpf("145.382.206-20"))  # Valid CPF from the example
        self.assertTrue(validate_cpf("529.982.247-25"))
        self.assertTrue(validate_cpf("52998224725"))

    def test_valid_cpf_generator(self):
        """
        This test will generate 10 valid CPFs and check if they are valid.
        Alsto generates 10 formatted CPFs and checks if they are valid.
        """
        for _ in range(10):
            cpf = generate_cpf()
            self.assertTrue(validate_cpf(cpf))
        for _ in range(10):
            cpf = generate_cpf(formatted=True)
            self.assertTrue(validate_cpf(cpf))

    def test_invalid_first_digit(self):
        with self.assertRaises(InvalidCPFError) as context:
            validate_cpf("145.382.206-30")  # Altered first verification digit
        self.assertIn("First verification digit does not match", str(context.exception))

    def test_invalid_second_digit(self):
        with self.assertRaises(InvalidCPFError) as context:
            validate_cpf("145.382.206-21")  # Altered second verification digit
        self.assertIn("Second verification digit does not match", str(context.exception))

    def test_repeated_digits_cpf(self):
        with self.assertRaises(RepeatedDigitsCPFError):
            validate_cpf("111.111.111-11")
        with self.assertRaises(RepeatedDigitsCPFError):
            validate_cpf("22222222222")
    
    def test_invalid_characters_cpf(self):
        with self.assertRaises(InvalidLengthCPFError):
            validate_cpf("529.982.247-2")

    def test_invalid_length_cpf(self):
        with self.assertRaises(InvalidLengthCPFError):
            validate_cpf("529.982.247-2")
        with self.assertRaises(InvalidLengthCPFError):
            validate_cpf("529.982.247-255")
    
    def test_whitespace_cpf(self):
        self.assertTrue(validate_cpf(" 145.382.206-20 "))
    
    def test_clean_cpf(self):
        cpf_formatted = format_cpf("14538220620")
        self.assertEqual(cpf_formatted, "145.382.206-20")
    
    def test_format_invalid_length_cpf(self):
        with self.assertRaises(InvalidLengthCPFError):
            clean_cpf("1453822062")  # Only 10 digits
    
    def test_format_invalid_characters_cpf(self):
        with self.assertRaises(InvalidFormatCPFError):
            clean_cpf("145.382.206-2A")
    
    def test_all_same_digits(self):
        with self.assertRaises(RepeatedDigitsCPFError):
            validate_cpf("000.000.000-00")
        with self.assertRaises(RepeatedDigitsCPFError):
            validate_cpf("99999999999")


if __name__ == '__main__':
    unittest.main()
