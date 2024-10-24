from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='br-eval',
    version='1.0.1',
    description='Library for validation and formatting of Brazilian data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Silvio Machado',
    author_email='silvio.machado@gmail.com',
    url='https://github.com/silvio-machado/br-eval',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
