import unittest
from br_eval.exceptions.plate_exceptions import (
    InvalidCharacterPlateError,
    InvalidLengthPlateError,
    InvalidPlateError
)
from br_eval.plate import (
    format_plate,
    generate_mercosul_car_plate,
    generate_mercosul_motorcycle_plate,
    generate_old_plate,
    validate_plate
)


class TestPlate(unittest.TestCase):
    def test_valid_old_plate(self):
        self.assertEqual(validate_plate('ABC1234'), 'Old')
        self.assertEqual(validate_plate('abc1234'), 'Old')
        self.assertEqual(validate_plate('ABC-1234'), 'Old')

    def test_valid_mercosul_car_plate(self):
        self.assertEqual(validate_plate('ABC1D23'), 'Mercosul Car')
        self.assertEqual(validate_plate('abc1d23'), 'Mercosul Car')
        self.assertEqual(validate_plate('ABC-1D23'), 'Mercosul Car')

    def test_valid_mercosul_motorcycle_plate(self):
        self.assertEqual(validate_plate('ABC12D3'), 'Mercosul Motorcycle')
        self.assertEqual(validate_plate('abc12d3'), 'Mercosul Motorcycle')
        self.assertEqual(validate_plate('ABC-12D3'), 'Mercosul Motorcycle')

    def test_invalid_plate_length(self):
        with self.assertRaises(InvalidLengthPlateError):
            validate_plate('AB1234')
        with self.assertRaises(InvalidLengthPlateError):
            validate_plate('ABCDEFGH')

    def test_invalid_plate_characters(self):
        with self.assertRaises(InvalidCharacterPlateError):
            validate_plate('AB@1234')
        with self.assertRaises(InvalidCharacterPlateError):
            validate_plate('ABC12*3')

    def test_invalid_plate_pattern(self):
        with self.assertRaises(InvalidPlateError):
            validate_plate('ABCD123')
        with self.assertRaises(InvalidPlateError):
            validate_plate('1234ABC')

    def test_format_plate(self):
        self.assertEqual(format_plate('ABC1234'), 'ABC-1234')
        self.assertEqual(format_plate('ABC1D23'), 'ABC-1D23')
        self.assertEqual(format_plate('ABC12D3'), 'ABC-12D3')

    def test_format_plate_invalid_length(self):
        with self.assertRaises(InvalidLengthPlateError):
            format_plate('ABC123')

    def test_generate_old_plate(self):
        for _ in range(100):
            plate = generate_old_plate()
            plate_type = validate_plate(plate)
            self.assertEqual(plate_type, 'Old')

    def test_generate_mercosul_car_plate(self):
        for _ in range(100):
            plate = generate_mercosul_car_plate()
            plate_type = validate_plate(plate)
            self.assertEqual(plate_type, 'Mercosul Car')

    def test_generate_mercosul_motorcycle_plate(self):
        for _ in range(100):
            plate = generate_mercosul_motorcycle_plate()
            plate_type = validate_plate(plate)
            self.assertEqual(plate_type, 'Mercosul Motorcycle')

    def test_generate_plate_formatted(self):
        plate = generate_old_plate(formatted=True)
        self.assertEqual(len(plate), 8)  # 'ABC-1234'
        plate_type = validate_plate(plate)
        self.assertEqual(plate_type, 'Old')


if __name__ == '__main__':
    unittest.main()
