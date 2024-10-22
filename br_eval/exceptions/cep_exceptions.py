class CEPError(Exception):
    """Base class for CEP exceptions."""
    pass


class InvalidCEPError(CEPError):
    """Exception for invalid CEPs."""
    def __str__(self):
        return "Invalid CEP format."


class InvalidLengthCEPError(CEPError):
    """Exception for CEPs with incorrect number of digits."""
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"CEP must have 8 digits. Current length: {self.length}."


class InvalidCharacterCEPError(CEPError):
    """Exception for CEPs with invalid characters."""
    def __str__(self):
        return "CEP must contain only numbers."
