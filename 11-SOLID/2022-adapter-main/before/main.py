"""
Loads config settings from json file and run fake experiment with them 
"""

import json

from experiment import Experiment


def main() -> None:
    with open("/Users/sahil/Desktop/Study/PythonTips/11-SOLID/2022-adapter-main/before/config.json", encoding="utf8") as file:
        config = json.load(file)
    experiment = Experiment(config)
    experiment.run()


if __name__ == "__main__":
    main()
