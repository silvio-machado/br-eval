import unittest
from br_eval.phone import (
    validate_phone_number,
    format_phone_number,
    generate_phone_number,
    clean_phone_number
)
from br_eval.exceptions.phone_exceptions import (
    InvalidPhoneNumberError,
    InvalidLengthPhoneNumberError,
    InvalidCharacterPhoneNumberError,
    InvalidDDDPhoneNumberError
)

class TestPhoneNumber(unittest.TestCase):
    def test_valid_mobile_numbers(self):
        self.assertEqual(
            validate_phone_number('11987654321')['type'],
            'mobile'
        )
        self.assertEqual(
            validate_phone_number('+55 (21) 99876-5432')['type'],
            'mobile'
        )
        self.assertEqual(
            validate_phone_number('61 9 9876-5432')['type'],
            'mobile'
        )
    
    def test_valid_landline_numbers(self):
        self.assertEqual(
            validate_phone_number('1131234567')['type'],
            'landline'
        )
        self.assertEqual(
            validate_phone_number('(31) 3123-4567')['type'],
            'landline'
        )
    
    def test_invalid_characters(self):
        with self.assertRaises(InvalidCharacterPhoneNumberError):
            validate_phone_number('(11) 9a876-5432')
    
    def test_invalid_length(self):
        with self.assertRaises(InvalidLengthPhoneNumberError):
            validate_phone_number('12345')
        with self.assertRaises(InvalidLengthPhoneNumberError):
            validate_phone_number('123456789012')
    
    def test_invalid_ddd(self):
        with self.assertRaises(InvalidDDDPhoneNumberError):
            validate_phone_number('00123456789')
    
    def test_invalid_number_pattern(self):
        with self.assertRaises(InvalidLengthPhoneNumberError):
            validate_phone_number('119123456')  # Incorrect length
        with self.assertRaises(InvalidPhoneNumberError):
            validate_phone_number('11812345678')  # Mobile number not starting with '9'

    
    def test_format_phone_number(self):
        formatted = format_phone_number('11987654321')
        self.assertEqual(formatted, '(11) 98765-4321')
    
    def test_generate_phone_number(self):
        for _ in range(100):
            number = generate_phone_number(phone_type='mobile')
            result = validate_phone_number(number)
            self.assertEqual(result['type'], 'mobile')
        
        for _ in range(100):
            number = generate_phone_number(phone_type='landline')
            result = validate_phone_number(number)
            self.assertEqual(result['type'], 'landline')
    
    def test_clean_phone_number(self):
        cleaned = clean_phone_number('+55 (11) 98765-4321')
        self.assertEqual(cleaned, '5511987654321')


if __name__ == '__main__':
    unittest.main()
