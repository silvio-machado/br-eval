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

__all__ = [
    'CPFError', 'InvalidCPFError', 'RepeatedDigitsCPFError',
    'InvalidFormatCPFError', 'InvalidLengthCPFError',
    'CNPJError', 'InvalidCNPJError', 'RepeatedDigitsCNPJError',
    'InvalidFormatCNPJError', 'InvalidLengthCNPJError'
]
