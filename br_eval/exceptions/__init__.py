from .cpf_exceptions import (
    CPFError,
    InvalidCPFError,
    RepeatedDigitsCPFError,
    InvalidFormatCPFError,
    InvalidLengthCPFError
)

from .cnpj_exceptions import (
    CNPJError,
    InvalidCNPJError,
    RepeatedDigitsCNPJError,
    InvalidFormatCNPJError,
    InvalidLengthCNPJError
)

from .plate_exceptions import (
    PlateError,
    InvalidPlateError,
    InvalidFormatPlateError,
    InvalidCharacterPlateError,
    InvalidLengthPlateError
)

from .cep_exceptions import (
    CEPError,
    InvalidCEPError,
    InvalidLengthCEPError,
    InvalidCharacterCEPError
)

# This list is used in the __all__ variable to define what symbols are exported
__all__ = [
    'CPFError', 'InvalidCPFError', 'RepeatedDigitsCPFError',
    'InvalidFormatCPFError', 'InvalidLengthCPFError',
    'CNPJError', 'InvalidCNPJError', 'RepeatedDigitsCNPJError',
    'InvalidFormatCNPJError', 'InvalidLengthCNPJError',
    'PlateError', 'InvalidPlateError', 'InvalidFormatPlateError',
    'InvalidCharacterPlateError', 'InvalidLengthPlateError',
    'CEPError', 'InvalidCEPError', 'InvalidLengthCEPError',
    'InvalidCharacterCEPError'
]
