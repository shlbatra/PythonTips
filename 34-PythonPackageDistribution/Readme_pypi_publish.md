- source 
    - https://realpython.com/pypi-publish-python-package/
- PyPI, Python Packaging Index,is a repository containing several hundred thousand packages. 
- The Python Packaging Index (PyPI) came online in 2003, originally as a pure index of existing packages, without any hosting capabilities.
- Ex. Python Structure
realpython-reader/
│
├── src/
│   └── reader/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.toml
│       ├── feed.py
│       └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── LICENSE
├── MANIFEST.in
├── README.md
└── pyproject.toml
- python module.py and python -m module are mostly equivalent
    - python -m is used to execute a module or a package.
    - python -m reader 0
    - When you run a package with -m, the file __main__.py within the package is executed
-  __main__.py acts as the entry point of your program and takes care of the main flow, calling other parts as needed:
- __init__.py -> put package constants, documentation. Variables defined in __init__.py become available as variables in the package namespace
- python -m hello (call module hello.py file)
- python -m reader (you can call the reader package with -m as long as the reader/ directory is available in your working directory - calls __main__.py file defined within package)

- Prepare Your Package for Publication
- PyPI name does not need to match the package name
    - Ex. pip install realpython-reader and then import reader
- Configure Your Package
    - Configuration of your build system
    - Configuration of your package
- A build system is responsible for creating the actual files that you’ll upload to PyPI, typically in the wheel or the source distribution (sdist) format
- Ex. pyproject.toml using setuptools ->
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"
- it’s usually better to use a declarative configuration file to express how to build your package, as it’s more straightforward to reason about and comes with fewer pitfalls to worry about. Using setup.cfg is the most common way to configure Setuptools. But as per PEP 621, 
pyproject.toml will be used for all your package configuration

Ex. code for pyproject.toml with all metadata -> 
# pyproject.toml

[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "realpython-reader"
version = "1.0.0"
description = "Read the latest Real Python tutorials"
readme = "README.md"
authors = [{ name = "Real Python", email = "info@realpython.com" }]
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["feed", "reader", "tutorial"]
dependencies = [
    "feedparser >= 5.2.0",
    "html2text",
    'tomli; python_version < "3.11"',
]
requires-python = ">=3.9"

[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

[project.urls]
Homepage = "https://github.com/realpython/reader"

[project.scripts]
realpython = "reader.__main__:main"

-> project.scripts creates command-line scripts that call functions within your package. Here, the new realpython command calls main() within the reader.__main__ module. The project.scripts table is one of three tables that can handle entry points. You can also include project.gui-scripts and project.entry-points, which specify GUI applications and plugins, respectively.

- dependencies 
you should strive to only specify the minimum requirements needed for your library or application to work. This list will be used by pip to resolve dependencies any time your package is installed. 

-  You pin your dependencies to make sure your environment is reproducible. Your package, on the other hand, should hopefully work across many different Python environments.

- The pip-tools project is a great way to manage pinned dependencies. It comes with a pip-compile command that can create or update a complete list of dependencies.
- Ex. pip-compile pyproject.toml -> pip-compile creates a detailed requirements.txt file
- use pip install or pip-sync to install these depedencies 

- project.optional-dependencies -> specify optional dependencies of your package in a separate table, 
- Ex.
[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]
- By default, optional dependencies aren’t included when a package is installed. However, by adding the group name in square brackets when running pip, you can manually specify that they should be installed. 
- install by command ->  pip install realpython-reader[dev]
- install with pip compile -> pip-compile --extra dev pyproject.toml

- Document Your Package
- At a minimum, you should include a README file with your project. 

- Test Your Package
- You can control exactly what’s included in your package by using find directives in pyproject.toml so tests are excluded 

- Version Your Package
- Your package needs to have a version. 
- Semantic versioning is a good default scheme to use,
- You specify the version as three numerical components, for instance 1.2.3. The components are called MAJOR, MINOR, and PATCH, respectively. 
- Rules for version increment : 
    Increment the MAJOR version when you make incompatible API changes.
    Increment the MINOR version when you add functionality in a backwards compatible manner.
    Increment the PATCH version when you make backwards compatible bug fixes.
- you want to specify the version number in different files within your project. For example, the version number is mentioned in both pyproject.toml and reader/__init__.py in the reader package. 
    - Use bumpver - bumpver init
    - For BumpVer to work properly, you must specify all files that contain your version number in the file_patterns subsection.
    - TOML file :
        [tool.bumpver]
        current_version = "1.0.0"
        version_pattern = "MAJOR.MINOR.PATCH"
        commit_message  = "Bump version {old_version} -> {new_version}"
        commit          = true
        tag             = true
        push            = false

        [tool.bumpver.file_patterns]
        "pyproject.toml" = ['current_version = "{version}"', 'version = "{version}"']
        "src/reader/__init__.py" = ["{version}"]
    - bumpver update --minor

- Add Resource Files to Your Package
- Examples include data files, binaries, documentation, and—as you have in this example—configuration files. Need to add them in manifest.in
- If you have other resource files and need to update the manifest, then you need to create a file named MANIFEST.in next to pyproject.toml in your project’s base directory. This file specifies rules for which files to include and which files to exclude
    - Ex.
    # MANIFEST.in

    include src/reader/*.toml

- License Your Package
- If you’re sharing your package with others, then you need to add a license to your package that explains how others are allowed to use your package. 
- You should add a file named LICENSE to your project that contains the text of the license you choose.

- Install Your Package Locally
- Editable Installs - This is a way of using pip to install your package locally in a way that lets you edit your code after it’s installed.
- Normally, pip does a regular install, which places a package into your site-packages/ folder.
Editable installs work around this by linking directly to your source code.
- Ex.  python -m pip install -e .
- you want to install the package located in the current working directory. In general, this should be the path to the directory containing your pyproject.toml file.
- You may get an error message saying “Project file has a ‘pyproject.toml’ and its build backend is missing the ‘build_editable’ hook.” You can work around this by adding a file named setup.py with the following contents:

# setup.py
from setuptools import setup
setup()

- Publish Your Package to PyPI
- To build and upload your package to PyPI, you’ll use two tools called Build and Twine. 
    - python -m pip install build twine

- Build Your Package
- Packages are wrapped into distribution packages. The most common formats for distribution packages are source archives and Python wheels.
- A source archive consists of your source code and any supporting files wrapped into one tar file. Similarly, a wheel is essentially a zip archive containing your code. You should provide both source archives and wheels for your package. Wheels are usually faster and more convenient for your end users, while source archives provide a flexible backup alternative.
    - python -m build   (builds source archive and wheels for your package)
    - You can find them in a newly created dist directory:
- Inspect wheel file as - 
        (venv) PS> cd .\dist
        (venv) PS> Copy-Item .\realpython_reader-1.0.0-py3-none-any.whl reader-whl.zip
        (venv) PS> Expand-Archive reader-whl.zip
        (venv) PS> tree .\reader-whl\ /F
- Twine can also check that your package description will render properly on PyPI.
    - twine check dist/*
- Upload Your Package to testpypi
    - twine upload -r testpypi dist/*
- Install package from testpypi
    - python -m pip install -i https://test.pypi.org/simple realpython-reader
- Upload your package to pypi
    - twine upload dist/*
- Go to project page -> pypi.org/project/your-package-name/
- Install Your Package
    - python -m pip install your-package-name

- Explore Other Build Systems

- Flit
- Flit doesn’t support advanced packages like those creating C extensions, and in general, it doesn’t give you many choices when setting up your package. Instead, Flit subscribes to the philosophy that there should be one obvious workflow to publish a package.
- python -m pip install flit
- flit init (Flit automates the preparations that you need to do with your package.)
generates pyproject.toml file as :
# pyproject.toml

[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "realpython-reader"
authors = [{ name = "Real Python", email = "info@realpython.com" }]
readme = "README.md"
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
dynamic = ["version", "description"]    (Flit actually figures these out itself by using __version__ and the docstring defined in the __init__.py file.)

[project.urls]
Home = "https://github.com/realpython/reader"

[project.scripts]
realpython = "reader.__main__:main"

- flit build   (build wheels and sdist in dist folder)
- flit publish  (publish to pypi)

- Poetry
- Poetry has more features that can help you during the development of your packages, including powerful dependency management.
- poetry init (This will create a pyproject.toml file based on your answers )
# pyproject.toml

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "realpython-reader"
version = "1.0.0"
description = "Read the latest Real Python tutorials"
authors = ["Real Python <info@realpython.com>"]
readme = "README.md"
homepage = "https://github.com/realpython/reader"
license = "MIT"

[tool.poetry.dependencies]
python = ">=3.9"
feedparser = "^6.0.8"
html2text = "^2020.1.16"
tomli = "^2.0.1"

[tool.poetry.scripts]
realpython = "reader.__main__:main"

- poetry build  (dist with wheels and sdist files)
- poetry publish

- Poetry can help you start a new project with the new command. It also supports working with virtual environments.