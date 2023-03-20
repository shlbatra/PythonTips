"""A simple plugin loader."""
import importlib  # import python scripts dyanmically

#need entrypoint to load plugin -> plugin register new classes in factory -> use dyanimically in game 

class ModuleInterface:
    """Represents a plugin interface. A plugin has a single register function."""
    #to add plugin to system, need to define this register method below
    @staticmethod
    def register() -> None:
        """Register the necessary items in the game character factory."""


def import_module(name: str) -> ModuleInterface:
    """Imports a module given a name."""
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    """Loads the plugins defined in the plugins list dyanmically."""
    for plugin_file in plugins:
        plugin = import_module(plugin_file)
        plugin.register()
