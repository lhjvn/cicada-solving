#!/usr/bin/env fish

# Activate my virtual environment
source /home/$USER/cicada-3301/bin/activate.fish

# Add the current directory to PYTHONPATH to make imports work
set -x PYTHONPATH $PYTHONPATH (pwd)

# Print environment info
echo "Python environment set up for Cicada 3301 analysis"
echo "PYTHONPATH: $PYTHONPATH"
python -c "import sys; print(f'Python version: {sys.version}')"
echo "Starting tests..."
cd src
python -m unittest discover -s testing
cd ..
echo "Ready and set."
