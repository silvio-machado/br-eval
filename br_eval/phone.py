import random
import re
from .exceptions.phone_exceptions import (
    InvalidPhoneNumberError,
    InvalidLengthPhoneNumberError,
    InvalidCharacterPhoneNumberError,
    InvalidDDDPhoneNumberError
)

# List of valid DDD codes
VALID_DDD_CODES = {
    '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '21', '22', '24',
    '27', '28',
    '31', '32', '33', '34', '35', '37', '38',
    '41', '42', '43', '44', '45', '46', '47', '48', '49',
    '51', '53', '54', '55',
    '61', '62', '64',
    '63',
    '65', '66',
    '67',
    '68',
    '69',
    '71', '73', '74', '75', '77',
    '79',
    '81', '87',
    '82',
    '83',
    '84',
    '85', '88',
    '86', '89',
    '91', '93', '94',
    '92', '97',
    '95',
    '96',
    '98', '99',
}


def clean_phone_number(phone_number: str) -> str:
    """
    Removes all non-digit characters from the phone number.
    Raises InvalidCharacterPhoneNumberError if letters are present.

    Args:
        phone_number (str): The phone number to clean.

    Returns:
        str: The cleaned phone number containing only digits.

    Raises:
        InvalidCharacterPhoneNumberError: If the phone number contains letters.
    """
    # Check for letters in the input
    if re.search(r'[a-zA-Z]', phone_number):
        raise InvalidCharacterPhoneNumberError(
            "Phone number contains letters."
        )
    return re.sub(r'\D', '', phone_number)


def validate_phone_number(phone_number):
    """
    Validates a Brazilian phone number.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        dict: A dictionary with keys 'type' and 'formatted_number'.
              'type' can be 'mobile' or 'landline'.

    Raises:
        InvalidLengthPhoneNumberError
        InvalidCharacterPhoneNumberError
        InvalidDDDPhoneNumberError
        InvalidPhoneNumberError
    """
    cleaned_number = clean_phone_number(phone_number)

    # Check if the number contains only digits
    if not cleaned_number.isdigit():
        raise InvalidCharacterPhoneNumberError()

    # Remove country code if present
    if cleaned_number.startswith('55') and len(cleaned_number) in (12, 13):
        cleaned_number = cleaned_number[2:]

    # Validate length
    if len(cleaned_number) not in (10, 11):
        raise InvalidLengthPhoneNumberError(len(cleaned_number))

    # Extract DDD and phone number
    ddd = cleaned_number[:2]
    number = cleaned_number[2:]

    # Validate DDD
    if ddd not in VALID_DDD_CODES:
        raise InvalidDDDPhoneNumberError(ddd)

    # Validate phone number
    if len(number) == 9 and number.startswith('9'):
        phone_type = 'mobile'
    elif len(number) == 8 and number[0] in '2345':
        phone_type = 'landline'
    else:
        raise InvalidPhoneNumberError(
            "Phone number does not match mobile or landline patterns."
        )

    return {
        'type': phone_type,
        'ddd': ddd,
        'number': number
    }


def format_phone_number(phone_number, international=False):
    """
    Formats the phone number into a standard format.

    Args:
        phone_number (str): The phone number to format.
        international (bool): If True, includes the country code '+55'.

    Returns:
        str: The formatted phone number.
    """
    validation_result = validate_phone_number(phone_number)
    ddd = validation_result['ddd']
    number = validation_result['number']

    if validation_result['type'] == 'mobile':
        formatted_number = f"({ddd}) {number[:5]}-{number[5:]}"
    else:
        formatted_number = f"({ddd}) {number[:4]}-{number[4:]}"

    if international:
        formatted_number = f"+55 {formatted_number}"

    return formatted_number


def generate_phone_number(
        phone_type='mobile', formatted=False, international=False
):
    """
    Generates a valid Brazilian phone number.

    Args:
        phone_type (str): 'mobile' or 'landline'.
        formatted (bool): If True, returns the formatted phone number.
        international (bool): If True, includes the country code '+55'.

    Returns:
        str: The generated phone number.
    """
    ddd = random.choice(list(VALID_DDD_CODES))

    if phone_type == 'mobile':
        # Mobile numbers start with '9' and have 9 digits
        number = '9' + ''.join(random.choices('0123456789', k=8))
    elif phone_type == 'landline':
        # Landline numbers start with digits from '2' to '5' and have 8 digits
        first_digit = random.choice('2345')
        number = first_digit + ''.join(random.choices('0123456789', k=7))
    else:
        raise ValueError("phone_type must be 'mobile' or 'landline'")

    full_number = ddd + number

    if formatted:
        full_number = format_phone_number(
            full_number,
            international=international
        )
    elif international:
        full_number = '55' + full_number

    return full_number
