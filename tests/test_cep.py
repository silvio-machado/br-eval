import unittest
from br_eval.cep import validate_cep, format_cep, clean_cep, generate_cep
from br_eval.exceptions.cep_exceptions import (
    InvalidLengthCEPError,
    InvalidCharacterCEPError
)

class TestCEP(unittest.TestCase):
    def test_valid_cep(self):
        self.assertTrue(validate_cep('01001-000'))
        self.assertTrue(validate_cep('30140071'))
        self.assertTrue(validate_cep('01001000'))

    def test_invalid_length_cep(self):
        with self.assertRaises(InvalidLengthCEPError):
            validate_cep('1234567')
        with self.assertRaises(InvalidLengthCEPError):
            validate_cep('123456789')

    def test_invalid_character_cep(self):
        with self.assertRaises(InvalidCharacterCEPError):
            validate_cep('01A01-000')
        with self.assertRaises(InvalidCharacterCEPError):
            validate_cep('ABCDE-FGH')
        with self.assertRaises(InvalidCharacterCEPError):
            validate_cep('94445abcx162')

    def test_format_cep(self):
        formatted = format_cep('01001000')
        self.assertEqual(formatted, '01001-000')

    def test_clean_cep(self):
        cleaned = clean_cep('01001-000')
        self.assertEqual(cleaned, '01001000')

    def test_generate_cep(self):
        for _ in range(100):
            cep = generate_cep()
            self.assertTrue(validate_cep(cep))

    def test_generate_formatted_cep(self):
        cep_formatted = generate_cep(formatted=True)
        self.assertEqual(len(cep_formatted), 9)
        self.assertEqual(cep_formatted[5], '-')
        self.assertTrue(validate_cep(cep_formatted))


if __name__ == '__main__':
    unittest.main()
