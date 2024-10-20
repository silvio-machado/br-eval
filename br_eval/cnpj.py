import random
import re
from .exceptions.cnpj_exceptions import (
    InvalidCNPJError,
    RepeatedDigitsCNPJError,
    InvalidFormatCNPJError,
    InvalidLengthCNPJError
)


def clean_cnpj(cnpj):
    """
    Removes all non-digit characters from the CNPJ.
    Raises an exception if the CNPJ does not have 14 digits after cleaning.
    """
    # Remove all non-digit characters
    cnpj_numbers = re.sub(r'\D', '', cnpj)

    # Verify if the CNPJ has exactly 14 digits
    if len(cnpj_numbers) != 14:
        raise InvalidLengthCNPJError(len(cnpj_numbers))

    # Check for invalid characters (should not contain letters)
    if not cnpj_numbers.isdigit():
        raise InvalidFormatCNPJError()

    return cnpj_numbers


def format_cnpj(cnpj):
    """
    Formats a CNPJ string into the pattern XX.XXX.XXX/YYYY-ZZ.

    Args:
        cnpj (str): The CNPJ string with exactly 14 digits.

    Returns:
        str: The formatted CNPJ string.

    Raises:
        InvalidLengthCNPJError: If the CNPJ does not have exactly 14 digits.
    """
    cnpj_numbers = clean_cnpj(cnpj)

    formatted_cnpj = f"{cnpj_numbers[:2]}.{cnpj_numbers[2:5]}."\
        f"{cnpj_numbers[5:8]}/{cnpj_numbers[8:12]}-{cnpj_numbers[12:]}"
    return formatted_cnpj


def validate_cnpj(cnpj):
    """
    Validates a CNPJ by checking the verification digits.
    Raises specific exceptions for different validation errors.

    Args:
        cnpj (str): The CNPJ string to validate.

    Returns:
        bool: True if the CNPJ is valid.

    Raises:
        RepeatedDigitsCNPJError: If all digits are the same.
        InvalidCNPJError: If the verification digits do not match.
    """
    cnpj_numbers = clean_cnpj(cnpj)

    # Check if all digits are the same
    if cnpj_numbers == cnpj_numbers[0] * 14:
        raise RepeatedDigitsCNPJError()

    original_verification_digits = cnpj_numbers[-2:]

    # Calculate the first verification digit
    weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_total = sum(int(cnpj_numbers[i]) * weights_first[i] for i in range(12))
    remainder = sum_total % 11
    first_digit = '0' if remainder < 2 else str(11 - remainder)

    # Calculate the second verification digit
    weights_second = [6] + weights_first
    sum_total = sum(
        int(cnpj_numbers[i]) * weights_second[i] for i in range(13)
    )
    remainder = sum_total % 11
    second_digit = '0' if remainder < 2 else str(11 - remainder)

    calculated_verification_digits = first_digit + second_digit

    if original_verification_digits != calculated_verification_digits:
        raise InvalidCNPJError("Verification digits do not match.")

    return True


def generate_cnpj(formatted=False):
    """
    Generates a valid CNPJ number.

    Args:
        formatted (bool):
            True, returns the CNPJ in the formatted pattern XX.XXX.XXX/YYYY-ZZ.
            False, returns the CNPJ as a numeric string.

    Returns:
        str: A valid CNPJ number.
    """
    # Generate the first twelve digits
    cnpj_numbers = [random.randint(0, 9) for _ in range(8)]
    cnpj_numbers += [0, 0, 0, 1]  # Commonly used for branch identifier

    # Calculate the first verification digit
    weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_total = sum(cnpj_numbers[i] * weights_first[i] for i in range(12))
    remainder = sum_total % 11
    first_digit = 0 if remainder < 2 else 11 - remainder

    cnpj_numbers.append(first_digit)

    # Calculate the second verification digit
    weights_second = [6] + weights_first
    sum_total = sum(cnpj_numbers[i] * weights_second[i] for i in range(13))
    remainder = sum_total % 11
    second_digit = 0 if remainder < 2 else 11 - remainder

    cnpj_numbers.append(second_digit)

    # Convert list of digits to string
    cnpj_str = ''.join(map(str, cnpj_numbers))

    if formatted:
        return format_cnpj(cnpj_str)
    else:
        return cnpj_str
