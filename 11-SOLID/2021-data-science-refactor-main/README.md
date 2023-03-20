# Data Science Project Refactoring

- Code write for data science makes sense
- easy to change and mantain
- reuse
- interpretability

- using protocol class as interface and its implementation 
- mixing datatypes - real numbers and floating point - be explicit. Add type hints everywhere
- not use variables and store intermediate results in them 
- for sequence use function composition - ex. Sequential in torch , pipeline in sklearn
- Create pipeline for data -> import, preprocess and export
- generic definition of pipeline and put it in seperate module/class
- use function composition for data pipeline

- Design Principle used in data science projects 
- Information Expert (part of GRASP)
    - assign responsibility to info expert 
    - design follow structure of the way the data follows \

- main has all the cod run expt and quite a lot of responsibilities
- understand where storing data and which part of program needs what kind of data
- create a seperate runner class that runs the training/test loop

- Config data and settings 
    - create constants required
- Data Loading Cleanup
    - how data is getting loaded in application
    - make sure no hidden parameters in other files that is not main
    - all parameters in single place
    - data configuration in main and not dat_load file
    - change config for diff data without modifying any other piece of code

- Design application around how data flows 
- info expert principle -runner class keeps track of metrics and intermediate datas 
- amount of data parameters that need to be passed between these modules should be minimized -> store process closer to data it needs
- Use type hints 







