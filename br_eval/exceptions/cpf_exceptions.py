class CPFError(Exception):
    """Base class for CPF exceptions."""
    pass


class InvalidCPFError(CPFError):
    """Exception raised when the CPF is invalid."""
    pass


class FirstDigitInvalidError(InvalidCPFError):
    """Exception raised when the first verification digit is incorrect."""
    def __str__(self):
        return "First verification digit does not match."


class SecondDigitInvalidError(InvalidCPFError):
    """Exception raised when the second verification digit is incorrect."""
    def __str__(self):
        return "Second verification digit does not match."


class RepeatedDigitsCPFError(InvalidCPFError):
    """Exception for CPFs with all digits equal."""
    def __str__(self):
        return "CPF cannot have all digits equal."


class InvalidFormatCPFError(CPFError):
    """Exception raised when the CPF contains non-numeric characters."""
    def __str__(self):
        return "CPF must contain only numbers."


class InvalidLengthCPFError(CPFError):
    """Exception raised when the CPF does not have 11 digits."""
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"CPF must have 11 digits. Current length: {self.length}."
