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

from .phone_exceptions import (
    PhoneNumberError,
    InvalidPhoneNumberError,
    InvalidLengthPhoneNumberError,
    InvalidCharacterPhoneNumberError,
    InvalidDDDPhoneNumberError
)

__all__ = [
    'CPFError', 'InvalidCPFError', 'RepeatedDigitsCPFError',
    'InvalidFormatCPFError', 'InvalidLengthCPFError',
    'CNPJError', 'InvalidCNPJError', 'RepeatedDigitsCNPJError',
    'InvalidFormatCNPJError', 'InvalidLengthCNPJError',
    'PlateError', 'InvalidPlateError', 'InvalidFormatPlateError',
    'InvalidCharacterPlateError', 'InvalidLengthPlateError',
    'CEPError', 'InvalidCEPError', 'InvalidLengthCEPError',
    'InvalidCharacterCEPError',
    'PhoneNumberError', 'InvalidPhoneNumberError',
    'InvalidLengthPhoneNumberError',
    'InvalidCharacterPhoneNumberError', 'InvalidDDDPhoneNumberError'
]
