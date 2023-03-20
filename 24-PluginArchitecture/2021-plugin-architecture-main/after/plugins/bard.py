"""Game extension that adds a bard character."""
#define custom plugin
from dataclasses import dataclass

from game import factory


@dataclass
class Bard:

    name: str
    instrument: str = "flute"

    def make_a_noise(self) -> None:
        print(
            f"I am {self.name} and I play the {self.instrument}. Toss a coin to your Witcher!"
        )

#define register for plugin
def register() -> None:
    #register new character to factory
    factory.register("bard", Bard)
