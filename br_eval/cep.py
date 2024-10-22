import random
import re
from .exceptions.cep_exceptions import (
    InvalidLengthCEPError,
    InvalidCharacterCEPError
)


def clean_cep(cep):
    """
    Remove all non-numeric characters from the CEP.
    Checks if the CEP has exactly 8 digits after cleaning.

    Args:
        cep (str): The CEP to be cleaned.

    Returns:
        str: The CEP containing only numeric digits.

    Raises:
        InvalidLengthCEPError: If the CEP does not have exactly 8 digits.
        InvalidCharacterCEPError: If the CEP contains letters.
    """
    # Checks if the CEP contains letters
    if re.search(r'[a-zA-Z]', cep):
        raise InvalidCharacterCEPError("CEP contains letters.")

    # Remove all non-numeric characters
    cep_numbers = re.sub(r'\D', '', cep)

    # Checks if the CEP has exactly 8 digits
    if len(cep_numbers) != 8:
        raise InvalidLengthCEPError(len(cep_numbers))

    # Checks if it contains only digits
    if not cep_numbers.isdigit():
        raise InvalidCharacterCEPError()

    return cep_numbers


def format_cep(cep):
    """
    Format the CEP in the 'XXXXX-XXX' pattern.

    Args:
        cep (str): The CEP containing 8 digits.

    Returns:
        str: The formatted CEP.

    Raises:
        InvalidLengthCEPError: If the CEP does not have exactly 8 digits.
    """
    cep_numbers = clean_cep(cep)
    formatted_cep = f"{cep_numbers[:5]}-{cep_numbers[5:]}"
    return formatted_cep


def validate_cep(cep):
    """
    Validate the CEP by checking if it is in the correct format.

    Args:
        cep (str): The CEP to be validated.

    Returns:
        bool: True if the CEP is valid.

    Raises:
        CEPError: Specific exceptions if the CEP is invalid.
    """
    clean_cep(cep)
    return True


def generate_cep(formatted=False):
    """
    Generate a valid random CEP.

    Args:
        formatted (bool): If True, returns the CEP formatted with a hyphen.

    Returns:
        str: The generated CEP.
    """
    cep_numbers = ''.join(random.choices('0123456789', k=8))
    if formatted:
        return format_cep(cep_numbers)
    else:
        return cep_numbers
