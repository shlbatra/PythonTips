- Once Python is installed, it creates a few directories on your system. The directories created depend on your operating system and the version of Python you have installed, but some common directories include:
    - bin: This directory contains the Python executable files.
    - include: This directory contains the header files needed to compile Python extensions.
    - lib: This directory contains the library files needed to link Python programs.
    - site-packages: This directory contains third-party modules installed using pip or other package managers.
    - documentation: This directory contains the Python documentation.

- You can find the location of these directories by running the following code in Python:
        import sys
        print(sys.prefix)
This will print the location of the Python installation directory on your system.

- get the path to the site-packages directory where Python packages are installed by default on a Mac
    python -c "import site; print(site.getsitepackages())"

- This command will display information about the package, including the location where it is installed. 
pip show -f <package-name>

- the PYTHONPATH environment variable is used to specify additional directories where Python should look for modules and packages that are not part of the standard library. Replace /path/to/your/python/modules with the path to the directory containing your Python modules. You can specify multiple directories by separating them with a colon :.
export PYTHONPATH=/path/to/your/python/modules:$PYTHONPATH
echo $PYTHONPATH
To make this setting persistent, you can add the above command to your shell's startup file, such as ~/.bashrc or ~/.bash_profile.

- 