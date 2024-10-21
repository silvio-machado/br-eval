# Validator Brazil

Python library for validation and formatting of Brazilian data such as:
- CPF
- CNPJ
- Vehicle license plates.
- Postal codes (CEP) # TODO
- Phone numbers # TODO

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

## Plate example

```python
from validator_brazil import validate_plate, format_plate

# Validate Plate
try:
    plate_type = validate_plate('ABC1234')
    print(f"Plate is valid. Type: {plate_type}")
except Exception as e:
    print(f"Invalid plate: {e}")

# Validate Mercosul Car Plate
try:
    plate_type = validate_plate('ABC1D23')
    print(f"Plate is valid. Type: {plate_type}")
except Exception as e:
    print(f"Invalid plate: {e}")

# Validate Mercosul Motorcycle Plate
try:
    plate_type = validate_plate('ABC12D3')
    print(f"Plate is valid. Type: {plate_type}")
except Exception as e:
    print(f"Invalid plate: {e}")

# Format Plate
formatted_plate = format_plate('ABC1D23')
print(f"Formatted Plate: {formatted_plate}")  # Output: 'ABC-1D23'
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# IMPORTANT NOTICE

Disclaimer 1: The CPF and CNPJ generator functions provided by this library are intended solely for development and testing purposes. The generated numbers do not correspond to real individuals or companies and should not be used in production systems, official registrations, or for any illegal or fraudulent activities. Misuse of these functions is the sole responsibility of the user.

Disclaimer 2: The vehicle plate generator functions provided in this library are intended solely for development and testing purposes. The generated plates do not correspond to real vehicles and should not be used in production systems, official documents, registrations, or any activities involving real-world entities. Misuse of these functions is the sole responsibility of the user.