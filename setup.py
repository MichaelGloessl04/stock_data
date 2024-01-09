from setuptools import setup, find_packages

setup(
    name='stock_importer',
    version='0.0.1',
    description='Import stock data and visualize it.',
    author='Michael Glössl',

    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pytest',
        'pandas',
        'matplotlib'
    ]
)
