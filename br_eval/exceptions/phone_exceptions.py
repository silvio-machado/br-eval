class PhoneNumberError(Exception):
    """Base class for phone number exceptions."""
    pass


class InvalidPhoneNumberError(PhoneNumberError):
    """Exception raised when the phone number is invalid."""
    def __str__(self):
        return "Invalid phone number format."


class InvalidLengthPhoneNumberError(PhoneNumberError):
    """Exception raised when the phone number has an invalid length."""
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Phone number has an invalid length: {self.length} digits."


class InvalidCharacterPhoneNumberError(PhoneNumberError):
    """Exception raised when the phone number contains invalid characters."""
    def __str__(self):
        return "Phone number must contain only digits."


class InvalidDDDPhoneNumberError(PhoneNumberError):
    """Exception raised when the DDD code is invalid."""
    def __init__(self, ddd):
        self.ddd = ddd

    def __str__(self):
        return f"Invalid DDD code: {self.ddd}."
