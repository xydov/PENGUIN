#! bin/bash

#usr/local/bin/penguin

#script used to install penguin

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
#python3 setup.py
#python3 setup.py install
pip install .

