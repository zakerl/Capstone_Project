Packages installed in python (UI side) has some issues sometimes while setting up.

To usually fix the "module not found, import error", follow theese steps:
1) Add __init__.py to both python_scripts as well as python_pyqt directories.
2) Run setup.py from python_pyqt using the following command: python setup.py install
3) Repeat for python_scripts, run python setup.py install