"""
Basic example of a Vehicle registration system.
"""
from dataclasses import dataclass
from enum import Enum, auto

# code smell 5 -> using wildcard imports as pollutes namespace in your module
# all fns not clear where coming from. just import specific things.
from random import *
from string import *


class FuelType(Enum):
    """Types of fuel used in a vehicle."""

    ELECTRIC = auto()
    PETROL = auto()


class RegistryStatus(Enum):
    """Possible statuses for the vehicle registry system."""

    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()


taxes = {FuelType.ELECTRIC: 0.02, FuelType.PETROL: 0.05}


@dataclass
class VehicleInfoMissingError(Exception):
    """Custom error that is raised when vehicle information is missing for a particular brand."""

    brand: str
    model: str
    message: str = "Vehicle information is missing."


@dataclass
class VehicleModelInfo:
    """Class that contains basic information about a vehicle model."""

    # code smell 6 -> using asymmetrical code ->doing same thing in diff ways
    # ex. get info string -> use built in dunder method __str__ in all cases
    brand: str
    model: str
    catalogue_price: int
    fuel_type: FuelType
    production_year: int

    @property
    def tax(self) -> float:
        """Tax to be paid when registering a vehicle of this type."""
        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def get_info_str(self) -> str:
        """String representation of this instance."""
        return f"brand: {self.brand} - type: {self.model} - tax: {self.tax}"


@dataclass
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)."""

    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def to_string(self) -> str:
        """String representation of this instance."""
        info_str = self.info.get_info_str()
        return f"Id: {self.vehicle_id}. License plate: {self.license_plate}. Info: {info_str}."


class VehicleRegistry:
    """Class representing a basic vehicle registration system."""

    # code smell 3 - not using right data structure, better to use dict than list for faster searching vehicle model info
    def __init__(self) -> None:
        self.vehicle_models: list[VehicleModelInfo] = []
        self.online = True

    # Code smell 1 -> too many parameters, copy all parameters from vehicle model info
    # code smell 2 -> feature envy -> object / method needs too many details of another object
    # accept vehicle model info object
    def add_vehicle_model_info(
        self,
        brand: str,
        model: str,
        catalogue_price: int,
        fuel_type: FuelType,
        year: int,
    ) -> None:
        """Helper method for adding a VehicleModelInfo object to a list."""
        self.vehicle_models.append(
            VehicleModelInfo(brand, model, catalogue_price, fuel_type, year)
        )

    # code smell 7 -> using self in methods that dont need it so turn them into static methods
    def generate_vehicle_id(self, length: int) -> str:
        """Helper method for generating a random vehicle id."""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """Helper method for generating a vehicle license number."""
        return f"{_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    # Too Deep Nesting
    # This method responsible to too many things,
    # using nested if with loops so better to split this -> find vehicle info amd create vehicle
    # handle special case for VehicleInfoMissingError(brand, model) before running the normal code

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate."""
        for vehicle_info in self.vehicle_models:
            if vehicle_info.brand == brand:
                if vehicle_info.model == model:
                    vehicle_id = self.generate_vehicle_id(12)
                    license_plate = self.generate_vehicle_license(vehicle_id)
                    return Vehicle(vehicle_id, license_plate, vehicle_info)
        raise VehicleInfoMissingError(brand, model)

    # Code smell 4 -> use nested conditional expressions - avoid
    # split them using regular if statement
    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        return (
            RegistryStatus.OFFLINE
            if not self.online
            else RegistryStatus.CONNECTION_ERROR
            if len(self.vehicle_models) == 0
            else RegistryStatus.ONLINE
        )


# Not using main fn -> evey variable available at module level so use
# seperate main()
if __name__ == "__main__":

    # create a registry instance
    registry = VehicleRegistry()

    # add a couple of different vehicle models
    registry.add_vehicle_model_info("Tesla", "Model 3", 50000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("Volkswagen", "ID3", 35000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("BMW", "520e", 60000, FuelType.PETROL, 2021)
    registry.add_vehicle_model_info("Tesla", "Model Y", 55000, FuelType.ELECTRIC, 2021)

    # verify that the registry is online
    print(f"Registry status: {registry.online_status()}")

    # register a new vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")

    # print out the vehicle information
    print(vehicle.to_string())
