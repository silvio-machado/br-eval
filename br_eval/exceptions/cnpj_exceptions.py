class CNPJError(Exception):
    """Base class for CNPJ exceptions."""
    pass


class InvalidCNPJError(CNPJError):
    """Exception raised when the CNPJ is invalid."""
    pass


class RepeatedDigitsCNPJError(InvalidCNPJError):
    """Exception for CNPJs with all digits equal."""
    def __str__(self):
        return "CNPJ cannot have all digits equal."


class InvalidFormatCNPJError(CNPJError):
    """Exception raised when the CNPJ contains invalid characters."""
    def __str__(self):
        return "CNPJ must contain only numbers."


class InvalidLengthCNPJError(CNPJError):
    """Exception raised when the CNPJ does not have 14 digits."""
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"CNPJ must have 14 digits. Current length: {self.length}."
