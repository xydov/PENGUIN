from setuptools import setup

setup(
    name='penguin',
    version='0.1',
    py_modules=['penguin'],
    install_requires=[
        'transformers',
        'torch',
        'Pillow',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'penguin=penguin:main',  # Use the main function
        ],
    },
)

