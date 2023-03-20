- Data Engineering Framework
- Boilerplate code -> common required procedures
    - auth pipelines 
    - I/O files (compress/decompress)
    - datetime 
    - logging setups 
    - querying in SQL dialect 
    - caching pipelines (ex. pickling)
    - testing and alerting setups 
- resusability 
- imp tools at single reference point
- mantainable pipeline in repo
- versioning info - reproducibility and flexibility
- shared and collaborated
- well documented
- significant and reliable head start 
- Framework steps 
    1. Gather most used data pipelines and fns in structued and documented manner
    2. Add them to remote repo
    3. Create installable package out of this repo
    4. Create template project with most common code structure and testing setup
    5. Clone template project at start of new project and install data engineering framework to kick start with all data engineering pipelines at hand 
- For step 5 
    a. Use the template package to start 
    b. Create Virtual Env 
    c. pip install requirements_etl -> install package and pytest
    d. detach remote from cloned repo (git remote remove origin )
    e. remove commit history (git checkout --orphan new_branch)
    f. commit branch with changes after pip install
    g. delete main branch git branch -D main 
    h. rename our branch as main - git branch -m main
    g. connect back to main branch - git remote add origin <https://.git>
    i. git push -u origin main
    j. test if package working   - python -c "import etl_pipelines"
- select interpretor created -> python virtual env 
    a. Go to main.py  -> from etl_pipelines.etl import LoggerOps








