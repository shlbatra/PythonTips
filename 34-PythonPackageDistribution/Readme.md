- Source article
    - https://medium.com/ochrona/understanding-python-package-distribution-types-25d53308a9a
- Python Package Distribution Types     
    - Wheels
    - Eggs
    - Source Distributions
- Primary Distribution Types
    - Python Source Distributions
        - A source distribution, or more commonly sdist, is a distribution that contains all of the python source code (i.e. .py files), any data files that the library requires, and a setup.py file which describes to the setuptools module how your python code should be packaged.
        - You can build an sdist distributable by running python setup.py sdist -> generate the distribution in the form of a tarball (i.e. a gzipped tar file).
        - Upon installation of an sdist, the setup.py file is executed on the host, ensuring that that package can be installed correctly.
    - Python Built Distribution
        - A built distribution, also sometimes referred to as a bdist, is slightly more complex in that it first pre-interprets or “builds” the package and critically cuts out the post-install setup.py build step that is necessary when using sdist.
        - 2 main types of bdist files
            - Eggs - old format, not used now 
            - Wheels    
            - Wheels and Eggs are both built distribution packaging formats that are meant to remove the need to build or compile a package, but instead provide a distributable that can be unpacked and used immediately.
            - Wheels utilize a standard naming structure which helps communicate their compatibility.
                    {dist}-{version}|-{build}|-{python}-{abi}-{platform}.whl
            - Assuming your package is pure python, this should be fairly easy to accomplish by running python setup.py sdist bdist_wheel

        - compiled python, commonly seen as .pyc files

- Source Article
    - https://packaging.python.org/en/latest/flow/
- Packaging and distributing projects
    - Publishing a package requires a flow from the author’s source code to an end user’s Python environment. The steps to achieve this are:
        - Have a source tree containing the package. This is typically a checkout from a version control system (VCS).
        - Prepare a configuration file describing the package metadata (name, version and so forth) and how to create the build artifacts. For most packages, this will be a pyproject.toml file, maintained manually in the source tree.
        - Create build artifacts to be sent to the package distribution service (usually PyPI); these will normally be a source distribution (“sdist”) and one or more built distributions (“wheels”). These are made by a build tool using the configuration file from the previous step. Often there is just one generic wheel for a pure Python package.
        - Upload the build artifacts to the package distribution service.

    - At that point, the package is present on the package distribution service. To use the package, end users must:

        - Download one of the package’s build artifacts from the package distribution service.
        - Install it in their Python environment, usually in its site-packages directory. This step may involve a build/compile step which, if needed, must be described by the package metadata.

    - The source tree
        - The particular version of the code used to create the build artifacts will typically be a checkout based on a tag associated with the version.
    - The configuration file
        - standard practice is to use a pyproject.toml file in the TOML format.
        - the pyproject.toml file needs a [build-system] table specifying your build tool. There are many build tools available, including but not limited to flit, hatch, pdm, poetry, setuptools, trampolim, and whey. Each tool’s documentation will show what to put in the [build-system] table
        - For example, here is a table for using hatch:
            [build-system]
            requires = ["hatchling"]
            build-backend = "hatchling.build"
        - Build artifacts
            - Source Distribution (sdist)
                A source distribution contains enough to install the package from source in an end user’s Python environment.
                Ex. python3 -m build --sdist source-tree-directory
            - Built Distribution (Wheels)
                A built distribution contains only the files needed for an end user’s Python environment. 
                No compilation steps are required during the install, and the wheel file can simply be unpacked into the site-packages directory.
                python3 -m build --wheel source-tree-directory
    - Upload to the package distribution service
        - twine tool. Ex 
            - twine upload dist/package-name-version.tar.gz dist/package-name-version-py3-none-any.whl
    - Download and install
        - python3 -m pip install package-name

- Source Article
    - https://packaging.python.org/en/latest/tutorials/installing-packages/
- Create virtual env using venv
    -   python3 -m venv tutorial_env
        source tutorial_env/bin/activate
    - packages are installed in site-packages folder. Ex. /usr/lib/python3.6/site-packages
    - Virtual Env have their own installation directories and they don’t share libraries with other virtual environments.
    - Ex. venv ->
                    python3 -m venv <DIR>
                    source <DIR>/bin/activate
    virtualenv -> 
                    python3 -m virtualenv <DIR>
                    source <DIR>/bin/activate

    - Pipenv tool automatically manages separate virtual environment for each project and application that you work on.
    - pip ex. python3 -m pip install "SomeProject==1.4"; python3 -m pip install "SomeProject~=1.4.2"
    - install from sdist or wheels, prefer wheels, avoid it by giving -no-binary option
    - If pip does not find a wheel to install, it will locally build a wheel and cache it for future installs
    - pip install from version control.
    Ex. python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
        python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch
    - install from extra index beyond pip 
    python3 -m pip install --extra-index-url http://my.package.repo/simple SomeProject

- Source Article
    - https://packaging.python.org/en/latest/tutorials/managing-dependencies/
    - Pipenv to manage dependencies for an application
    -  Pipenv is recommended for collaborative projects as it’s a higher-level tool that simplifies dependency management for common use cases.
    - Pipenv will install the Requests library and create a Pipfile for you in your project’s directory. The Pipfile is used to track which dependencies your project needs in case you need to re-install them, such as when you share your project with others. 
    Ex. cd myproject
        pipenv install requests
    - run script main.py using pipenv run python main.py

- Source Article
    - https://packaging.python.org/en/latest/tutorials/packaging-projects/
    - File Structure -
    packaging_tutorial/
        └── src/
            └── example_package_sahilbatra/
                ├── __init__.py
                └── example.py

    - Upload package to pypi -
      - Choose a memorable and unique name for your package. You don’t have to append your username as you did in the tutorial, but you can’t use an existing name.
      - Register an account on https://pypi.org - note that these are two separate servers and the login details from the test server are not shared with the main server.
      - Use twine upload dist/* to upload your package and enter your credentials for the account you registered on the real PyPI. Now that you’re uploading the package in production, you don’t need to specify --repository; the package will upload to https://pypi.org/ by default.
      - Install your package from the real PyPI using python3 -m pip install [your-package].

- Source Article 
    - https://packaging.python.org/en/latest/tutorials/creating-documentation/
- Creating Documentation using Sphinx

- install_requires vs requirements file 
- install_requires defines the dependencies for a single project, Requirements Files are often used to define the requirements for a complete Python environment.

- Source Article
    - https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- pip is the reference Python package manager. It’s used to install and update packages.
-  If you are using Python 3.3 or newer, the venv module is the preferred way to create and manage virtual environments. 
    - python3 -m venv env   (venv will create a virtual Python installation in the env folder.)
    - source env/bin/activate
    - which python (confirm activated env or not)  -> .../env/bin/python
    - deactivate (leave environment)
    - ex. pip install requests==2.18.4, install requests>=2.0.0,<3.0.0 -> install latest 2.x release
    - pip install --pre requests -> install pre-release version of package
    - pip install requests[security] -> installing optional extras
    - pip install . (install directly from source)
    - pip install --editable . (install packages in editable mode)
    - google-auth @ git+https://github.com/GoogleCloudPlatform/google-auth-library-python.git (pip install from git)
    - python3 -m pip install requests-2.18.4.tar.gz (install from local archive)
    - python3 -m pip install --no-index --find-links=/local/dir/ requests (install from local archives of multiple packages)
    - python3 -m pip install --index-url http://index.example.com/simple/ SomeProject (install from another index)
    - python3 -m pip install --extra-index-url http://index.example.com/simple/ SomeProject (install from additional index)
    - python3 -m pip install --upgrade requests (upgrade packages)

- Source Article
    - https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
- Distributing packages using setuptools
    - setup.py
        - It’s the file where various aspects of your project are configured. The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined. The most relevant arguments are explained in the section below.
        - It’s the command line interface for running various commands that relate to packaging tasks. To get a listing of available commands, run python setup.py --help-commands.
    - setup.cfg
        - setup.cfg is an ini file that contains option defaults for setup.py commands. 












