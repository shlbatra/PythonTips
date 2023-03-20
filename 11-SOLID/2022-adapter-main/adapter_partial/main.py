import json
from functools import partial

from bs4 import BeautifulSoup

from experiment import Experiment
from xml_adapter import get_from_bs


def main() -> None:

    with open("/Users/sahil/Desktop/Study/PythonTips/11-SOLID/2022-adapter-main/adapter_partial/config.json", encoding="utf8") as file:
        config = json.load(file)
    with open("/Users/sahil/Desktop/Study/PythonTips/11-SOLID/2022-adapter-main/adapter_partial/config.xml", encoding="utf8") as file:
        config_xml = file.read()
    soup = BeautifulSoup(config_xml, "html.parser")
    #partial takes existing fn and applies arguments to it and then returns new fn -> apply remaining args 
    bs_adapter_fn = partial(get_from_bs, soup) #use partial because callgetter expects string and returns any (Callable[[str], Any])
    #the function expects beautifulsoup and returns Any
    # experiment = Experiment(config.get) #pass callable here instead of class object, pass get method linked to config object
    experiment = Experiment(bs_adapter_fn)
    experiment.run()


if __name__ == "__main__":
    main()
