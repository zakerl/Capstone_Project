# EMAnator UI source code
The db folder is used to link python code with database and to test functionality. pyqt_ui folder contains all the .ui design files for pyqt designer. python_scripts is a python package and it contains all the backend python files to generate the UI.

Debugging Installation Issues:

Packages installed in python (UI side) has some issues sometimes while setting up.

To usually fix the "module not found, import error", follow theese steps:

Add init.py to both python_scripts as well as python_pyqt directories.
Run setup.py from python_pyqt using the following command: python setup.py install
Repeat for python_scripts, run python setup.py install
