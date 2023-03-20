# Configuration Management For Data Science Made Easy With Hydra

- Best place to store settings -> web scraping or data processing
- Not good practice to have config settings in code directly. Ex here - Hyperparameters or data configuration
- easy to reuse config settings by others if available in seperate place than code
- consistency that all config settings be at one place for mantaining code and readability
- if config settings outside code then change them without changing code
- if config outside, run experiment with diff config settings by providing a script that chooses config file
- Cohesion, Coupling and Configuration
    - 
- Dealing with Config Mgt hard ?
    - Need them at a lot of places in code
    - single place to define them to keep track of all settings
    - if store at single place, then pass them around everywhere - fns with lots of args -> weak cohesion
    - if config global variable -> lot of coupling, if config not there, code break as well
- Accessing config settings ?
    - define locally or in the file in which settings needed -> settings all over the code
    - env variables -> python.env package -> define env variables and code access those variables, change them without modifying code, create .env files -> env variables at one place, from code not directly easy to what config variables change and no structure (grouping) of variables 
    - use json / yaml -> contain specification of your settings,provide structure (sub objects) -> layers, use package hydra -> config in command line, config across files, config with sub objects for structure, batches of configs 
- hydra package
    - put all config settings in yaml file
    - conf contains all config settings
    - creates output folder - timestamped with when code last ran with configs used, so change working dir so make sure use cwd to pick from current working directory
    - type hinting -> use dataclass to define structure of config object
    - use multiple files and folders
    - _self_ -> for legacy issues. give preferential treatment to files defined in default instead of value in legacy stored
- Tips to deal with Config settings
    - define settings in single place - json/yaml - outside code
    - load and apply in main file
    - structure config settings - which settings used where , comments in yaml file
    - reuse config packages like hydra





