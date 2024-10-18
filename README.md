# Validator Brazil

Python library for validation and formatting of Brazilian data such as CPF, CNPJ, postal codes (CEP), phone numbers, and vehicle license plates.

## Installation

```bash
pip install br-eval
```

## Usage example

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

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.