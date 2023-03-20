1.  Create Virtual Env
    - python3 -m venv venv → creates a virtual environment
    - source venv/bin/activate → activates the environment
    - deactivate → deactivates the environment

2. Change python interpretor to Python Virtual Env

3. Freeze packages and save to reqts file
    - pip freeze > requirements.txt 
    - pip install -r requirements.txt

4. create separate directory for tests (Use Pytest)
    - Use __init__ in test folder to create test module where all test files are kept

5. Create different content directories
    - Create as many directories as you want with __init__ command
    - __init__.py is used to mark directories as Python package directories
    - Example code below :

            # if you have something like this:
            another_directory/__init__.py
            another_directory/module.py

            # you can import the code in module.py as
            from another_directory import module

            # or
            import another_directory.module

4. Document Your Code
    - Add a docstring with a description at the start of each file
    - Add a docstring to each function and class
    - Use type-hints whenever you define a function or a class -> allows to automatically check your code with mypy
    - Use GitHub for Version Control