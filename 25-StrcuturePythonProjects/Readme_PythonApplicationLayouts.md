- Source Article
    - Python Application Layouts: A Reference

- Command-Line Application Layouts
- Ex. a simple script that runs on its own. You’ll then see how to build up the layout as the use cases advance.
- Ex. structure
        helloworld/
        │
        ├── .gitignore
        ├── helloworld.py
        ├── LICENSE
        ├── README.md
        ├── requirements.txt
        ├── setup.py
        └── tests.py

- Installable Single Package
- Ex. Structure
        helloworld/
        │
        ├── helloworld/
        │   ├── __init__.py
        │   ├── helloworld.py
        │   └── helpers.py
        │
        ├── tests/
        │   ├── helloworld_tests.py
        │   └── helpers_tests.py
        │
        ├── .gitignore
        ├── LICENSE
        ├── README.md
        ├── requirements.txt
        └── setup.py

- The only difference here is that your application code is now all held in the helloworld subdirectory—this directory is named after your package—and that we’ve added a file called __init__.py. Let’s introduce these new files:
- helloworld/__init__.py: This file has many functions, but for our purposes it tells the Python interpreter that this directory is a package directory. You can set up this __init__.py file in a way that enables you to import classes and methods from the package as a whole, instead of knowing the internal module structure and importing from helloworld.helloworld or helloworld.helpers.

- Application with Internal Packages
- In larger applications, you may have one or more internal packages that are either tied together with a main runner script or that provide specific functionality to a larger library you are packaging. 
- Ex. structure

            helloworld/
            │
            ├── bin/
            │
            ├── docs/
            │   ├── hello.md
            │   └── world.md
            │
            ├── helloworld/
            │   ├── __init__.py
            │   ├── runner.py
            │   ├── hello/
            │   │   ├── __init__.py
            │   │   ├── hello.py
            │   │   └── helpers.py
            │   │
            │   └── world/
            │       ├── __init__.py
            │       ├── helpers.py
            │       └── world.py
            │
            ├── data/
            │   ├── input.csv
            │   └── output.xlsx
            │
            ├── tests/
            │   ├── hello
            │   │   ├── helpers_tests.py
            │   │   └── hello_tests.py
            │   │
            │   └── world/
            │       ├── helpers_tests.py
            │       └── world_tests.py
            │
            ├── .gitignore
            ├── LICENSE
            └── README.md

bin/: This directory holds any executable files. The most important point to remember is that your executable shouldn’t have a lot of code, just an import and a call to a main function in your runner script.
/docs: With a more advanced application, you’ll want to maintain good documentation of all its parts. 
data/: Having this directory is helpful for testing. It’s a central location for any files that your application will ingest or produce. 
tests/: Here, you can put all your tests—unit tests, execution tests, integration tests, and so on.

- Web Application Layouts
-  Django and Flask are arguably the most popular web frameworks for Python

- Django
- It will create a project skeleton for you after running django-admin startproject project, where project is the name of your project. Ex structure ->
        project/
        │
        ├── project/
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        │
        └── manage.py
In Django, this is a project, which ties together the other Django concept, apps. Apps are where logic, models, views, and so on all live, and in doing so they do some task, such as maintaining a blog.

Django apps can be imported into projects and used across projects, and are structured like specialized Python packages.
After you set up your project, all you have to do is navigate to the location of manage.py and run python manage.py startapp app, where app is the name of your app.

This will result in a directory called app with the following layout:
        app/
        │
        ├── migrations/
        │   └── __init__.py
        │
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        └── views.py

Final skeleton structure ->
        project/
        │
        ├── app/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   │
        │   ├── migrations/
        │   │   └── __init__.py
        │   │
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        │
        ├── docs/
        │
        ├── project/
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        │
        ├── static/
        │   └── style.css
        │
        ├── templates/
        │   └── base.html
        │
        ├── .gitignore
        ├── manage.py
        ├── LICENSE
        └── README.md

- Flask
- Flask is a Python web “microframework.”
- Ex structure of project ->

flaskr/
│
├── flaskr/
│   ├── ___init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   │
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   │ 
│   └── static/
│       └── style.css
│
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
│
├── venv/
│
├── .gitignore
├── setup.py
└── MANIFEST.in



















