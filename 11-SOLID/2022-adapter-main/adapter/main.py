from bs4 import BeautifulSoup

from experiment import Experiment
from xml_adapter import XMLAdapter


def main() -> None:
    with open("/Users/sahil/Desktop/Study/PythonTips/11-SOLID/2022-adapter-main/adapter/config.xml", encoding="utf8") as file:
        config_xml = file.read()
    bs_xml = BeautifulSoup(config_xml, "html.parser")
    adapter = XMLAdapter(bs_xml)
    experiment = Experiment(adapter)
    experiment.run()
    """For class version -> override get method for bs -> other things rely on bs might not work anymore - class dangerous
    adapter = XMLConfig(config, "xml")
    
    """


if __name__ == "__main__":
    main()
