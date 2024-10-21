class PlateError(Exception):
    """Base class for plate exceptions."""
    pass


class InvalidPlateError(PlateError):
    """Exception raised when the plate is invalid."""
    def __str__(self):
        return "Invalid plate format."


class InvalidFormatPlateError(PlateError):
    """Exception raised when the plate has invalid characters or length."""
    def __str__(self):
        return "Plate must be a string of 7 alphanumeric characters."


class InvalidCharacterPlateError(PlateError):
    """Exception raised when the plate contains invalid characters."""
    def __str__(self):
        return "Plate contains invalid characters."


class InvalidLengthPlateError(PlateError):
    """Exception raised when the plate does not have 7 characters."""
    def __str__(self):
        return "Plate must have exactly 7 characters."
