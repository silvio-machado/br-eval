import random
import re
import string
from .exceptions.plate_exceptions import (
    InvalidPlateError,
    InvalidFormatPlateError,
    InvalidCharacterPlateError,
    InvalidLengthPlateError
)


def validate_plate(plate):
    """
    Validates a Brazilian vehicle plate, considering old and new
    Mercosul standards.
    Raises specific exceptions for different validation errors.

    Args:
        plate (str): The plate string to validate.

    Returns:
        str: The type of plate validated (
            e.g., 'Old', 'Mercosul Car', 'Mercosul Motorcycle'
        ).

    Raises:
        InvalidLengthPlateError: If the plate does not have 7 characters.
        InvalidCharacterPlateError: If the plate contains invalid characters.
        InvalidPlateError: If the plate does not match any valid pattern.
    """
    if not isinstance(plate, str):
        raise InvalidFormatPlateError()

    plate = plate.upper().replace('-', '').strip()

    if len(plate) != 7:
        raise InvalidLengthPlateError()

    if not re.match(r'^[A-Z0-9]{7}$', plate):
        raise InvalidCharacterPlateError()

    # Patterns
    old_pattern = re.compile(r'^[A-Z]{3}[0-9]{4}$')
    mercosul_car_pattern = re.compile(r'^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}$')
    mercosul_motorcycle_pattern = re.compile(
        r'^[A-Z]{3}[0-9]{2}[A-Z]{1}[0-9]{1}$'
    )

    if old_pattern.match(plate):
        return 'Old'
    elif mercosul_car_pattern.match(plate):
        return 'Mercosul Car'
    elif mercosul_motorcycle_pattern.match(plate):
        return 'Mercosul Motorcycle'
    else:
        raise InvalidPlateError()


def format_plate(plate):
    """
    Formats the plate string by inserting a hyphen.

    Args:
        plate (str): The plate string to format.

    Returns:
        str: The formatted plate string (e.g., 'ABC-1234').
    """
    plate = plate.upper().replace('-', '').strip()
    if len(plate) != 7:
        raise InvalidLengthPlateError()

    return f"{plate[:3]}-{plate[3:]}"


def generate_old_plate(formatted=False):
    """
    Generates a valid vehicle plate in the old format (ABC1234).

    Args:
        formatted (bool): If True, returns the plate with a hyphen (ABC-1234).

    Returns:
        str: A generated vehicle plate.
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    plate = f"{letters}{numbers}"
    if formatted:
        plate = f"{letters}-{numbers}"
    return plate


def generate_mercosul_car_plate(formatted=False):
    """
    Generates a valid vehicle plate in the Mercosul car format (ABC1D23).

    Args:
        formatted (bool): If True, returns the plate with a hyphen (ABC-1D23).

    Returns:
        str: A generated vehicle plate.
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    first_number = random.choice(string.digits)
    middle_letter = random.choice(string.ascii_uppercase)
    last_numbers = ''.join(random.choices(string.digits, k=2))
    plate = f"{letters}{first_number}{middle_letter}{last_numbers}"
    if formatted:
        plate = f"{letters}-{first_number}{middle_letter}{last_numbers}"
    return plate


def generate_mercosul_motorcycle_plate(formatted=False):
    """
    Generates valid vehicle plate in the Mercosul motorcycle format (ABC12D3).

    Args:
        formatted (bool): If True, returns the plate with a hyphen (ABC-12D3).

    Returns:
        str: A generated vehicle plate.
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    first_numbers = ''.join(random.choices(string.digits, k=2))
    middle_letter = random.choice(string.ascii_uppercase)
    last_number = random.choice(string.digits)
    plate = f"{letters}{first_numbers}{middle_letter}{last_number}"
    if formatted:
        plate = f"{letters}-{first_numbers}{middle_letter}{last_number}"
    return plate


def generate_plate(plate_type='old', formatted=False):
    """
    Generates a vehicle plate of the specified type.

    Args:
        plate_type (str): Type of plate to generate (
            'old', 'mercosul_car', 'mercosul_motorcycle'
        ).
        formatted (bool): If True, returns the plate with a hyphen.

    Returns:
        str: A generated vehicle plate.

    Raises:
        ValueError: If the plate_type is not recognized.
    """
    if plate_type == 'old':
        return generate_old_plate(formatted)
    elif plate_type == 'mercosul_car':
        return generate_mercosul_car_plate(formatted)
    elif plate_type == 'mercosul_motorcycle':
        return generate_mercosul_motorcycle_plate(formatted)
    else:
        raise ValueError(f"Unknown plate type: {plate_type}")
