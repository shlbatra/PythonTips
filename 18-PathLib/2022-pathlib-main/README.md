- PathLib
- Before pathlib, python packages used strings to deal with paths
- issues with strings
    - pain to construct path ex. us os.join - hard to read
    - path represented diff across OS
    - info in path want access easily ex. file or dir
- object oriented way of dealing with paths
- paths objects and have useful operations / methods that can be perfomed
- r infront of string treats it as a raw string
- Common to set paths in config files 
    - folder where sample data
    - output log data
- data classes dont directly support converting path. Better to use pydantic