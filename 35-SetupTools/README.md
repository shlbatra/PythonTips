- Add a set of additional files containing metadata and configuration to not only instruct setuptools on how the distribution should be built but also to help installer (such as pip) during the installation process.
- pip install --upgrade build ( to run build command -> python -m build)
- provide build system info on pyproject.toml file ->
    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"
- Ex.
    pyproject.toml
    [project]
    name = "mypackage"
    version = "0.0.1"
    dependencies = [
        "requests",
        'importlib-metadata; python_version<"3.8"',
    ]

    setup.cfg
    [metadata]
    name = mypackage
    version = 0.0.1

    [options]
    install_requires =
        requests
        importlib-metadata; python_version < "3.8"



    setup.py
    from setuptools import setup
    setup(
        name='mypackage',
        version='0.0.1',
        install_requires=[
            'requests',
            'importlib-metadata; python_version == "3.8"',
        ],
    )

    - organize package as ->

    mypackage
    ├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
    |   # README.rst or README.md (a nice description of your package)
    |   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
    └── mypackage
        ├── __init__.py
        └── ... (other Python files)

    - Run command for build -> python -m build
