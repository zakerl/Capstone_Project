# EMAnator UI source code
The db folder is used to link python code with database and to test functionality. <br />pyqt_ui folder contains all the .ui design files for pyqt designer. <br />python_scripts is a python package and it contains all the backend python files to generate the UI.

python_handler folder contains all the source code for UI backend that is used to handle events for the UI.<br />
bed_mainwindow_handler.py is the main code that runs the main menu from python.

Debugging Installation Issues:

Packages installed in python (UI side) has some issues sometimes while setting up.

To usually fix the "module not found, import error", follow theese steps:

1) Add init.py to both python_scripts as well as python_pyqt directories.
2) Run setup.py from python_pyqt using the following command: python setup.py install
3) Repeat for python_scripts, run python setup.py install
