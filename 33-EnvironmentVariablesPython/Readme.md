- Source Article
    - https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
- Environment variables— variables that exist outside of your code as part of your server environment— can help you by both streamlining and making more secure the process of running your scripts and applications. 
- When to Use Python Environment Variables
    -  Common use cases for environment variables include authentication keys (API token) and execution mode (e.g. development, staging, production).
- How to Get Environment Variables With Python
    - See environment variables in your system ->
        import os
        print(os.environ)
    - Check current value for specific environment variables in your session
        os.environ.get('USER') -> if not matching key, return None
- How to Set Environment Variables in Python
    - It’s important to note that this changes the environment variable in this session. In other words, changing the environment variable here will not affect the environment variable anywhere else. 
        Ex. os.environ['USER'] = 'Bob'
            os.environ.pop('USER')   # clear single environment variable 
            os.environ.clear()       # clean all environment variables 
- If you need to permanently delete or set environment variables you will need to do so with a shell environment, such as Bash.
- How to Use dotenv Manage Environment Variables
    - use a library like dotenv to help manage lot of environment variables 
    - It allows you to set or update the environment variables for files in a specific directory by reading them in from another file.
    - dotenv reads in environment variables from a file named .env. The file should be formatted as follows:
            api-token = "abcdef_123456"

            Once that’s created and placed in the same folder as your Python file, environment variables can be called like so:

            From dotenv import load_dotenv
            load_dotenv()
            import os
            token = os.environ.get("api-token")