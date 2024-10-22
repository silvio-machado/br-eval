# Validator Brazil

Python library for validation and formatting of Brazilian data such as:
- CPF
- CNPJ
- Vehicle license plates.
- Postal codes (CEP)
- Phone numbers

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

## CEP example

```python
from br_eval.cep import validate_cep, format_cep, generate_cep

# Validate CEP
try:
    validate_cep('01001-000')
    print("CEP is valid.")
except Exception as e:
    print(f"Invalid CEP: {e}")

# Format CEP
formatted_cep = format_cep('01001000')
print(f"Formatted CEP: {formatted_cep}")

# Generate CEP
cep_generated = generate_cep(formatted=True)
print(f"Generated CEP: {cep_generated}")
```
*Note:* The CEP validator requires that the input contains only numeric characters. If the CEP contains letters or other invalid characters, it will raise an InvalidCharacterCEPError.

## Phone example

```python
from br_eval import (
    validate_phone_number,
    format_phone_number,
    generate_phone_number
)

# Validate Mobile Phone Number
try:
    result = validate_phone_number('(11) 98765-4321')
    print(f"Phone number is valid. Type: {result['type']}")
except Exception as e:
    print(f"Invalid phone number: {e}")

# Validate Landline Phone Number
try:
    result = validate_phone_number('21 3123-4567')
    print(f"Phone number is valid. Type: {result['type']}")
except Exception as e:
    print(f"Invalid phone number: {e}")

# Format Phone Number
formatted_number = format_phone_number('11987654321', international=True)
print(f"Formatted Phone Number: {formatted_number}")  # Output: '+55 (11) 98765-4321'

# Generate Mobile Phone Number
generated_mobile = generate_phone_number(phone_type='mobile', formatted=True)
print(f"Generated Mobile Phone Number: {generated_mobile}")

# Generate Landline Phone Number
generated_landline = generate_phone_number(phone_type='landline', formatted=True)
print(f"Generated Landline Phone Number: {generated_landline}")
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# IMPORTANT NOTICE

Disclaimer 1: The CPF and CNPJ generator functions provided by this library are intended solely for development and testing purposes. The generated numbers do not correspond to real individuals or companies and should not be used in production systems, official registrations, or for any illegal or fraudulent activities. Misuse of these functions is the sole responsibility of the user.

Disclaimer 2: The vehicle plate generator functions provided in this library are intended solely for development and testing purposes. The generated plates do not correspond to real vehicles and should not be used in production systems, official documents, registrations, or any activities involving real-world entities. Misuse of these functions is the sole responsibility of the user.

Disclaimer 3: The CEP generator function provided in this library is intended solely for development and testing purposes. The generated CEPs do not necessarily correspond to real addresses and should not be used in production systems, official documents, registrations, or any activities involving real-world entities. Misuse of this function is the sole responsibility of the user.

Disclaimer 4: The phone number generator functions provided in this library are intended solely for development and testing purposes. The generated phone numbers do not correspond to real individuals or active lines and should not be used in production systems, official documents, registrations, marketing campaigns, telemarketing activities, or any activities involving real-world entities. Misuse of these functions is the sole responsibility of the user.