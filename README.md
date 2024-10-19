# Validator Brazil

Python library for validation and formatting of Brazilian data such as:
- CPF
- CNPJ
- postal codes (CEP) # TODO
- phone numbers # TODO
- and vehicle license plates. # TODO

## Installation

```bash
pip install br-eval
```

# Usage example

## CPF

```python
from br_eval.cpf import validate_cpf, format_cpf

# Validate CPF
try:
    validate_cpf('145.382.206-20')
    print("CPF is valid.")
except Exception as e:
    print(f"Invalid CPF: {e}")

# Format CPF
formatted_cpf = format_cpf('14538220620')
print(f"Formatted CPF: {formatted_cpf}")
```

## CNPJ example

```python
from validator_brazil import validate_cnpj, format_cnpj

# Validate CNPJ
try:
    validate_cnpj('13.347.016/0001-17')
    print("CNPJ is valid.")
except Exception as e:
    print(f"Invalid CNPJ: {e}")

# Format CNPJ
formatted_cnpj = format_cnpj('13347016000117')
print(f"Formatted CNPJ: {formatted_cnpj}")
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.