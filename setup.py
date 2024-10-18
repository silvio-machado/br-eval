from setuptools import setup, find_packages

setup(
    name='br-eval',
    version='0.1.0',
    description='Library for validation and formatting of Brazilian data',
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
