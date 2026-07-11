from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from typing import Protocol


@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def distance_to(self, other: Coordinates) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


@dataclass(frozen=True)
class GeoFence:
    name: str


@dataclass(frozen=True)
class Route:
    start: Coordinates
    destination: Coordinates
    avoid_zones: list[GeoFence] = field(default_factory=list[GeoFence]) # Use default_factory instead of None


@dataclass(frozen=True)
class DroneTelemetry:
    drone_id: str
    location: Coordinates | None # For raw data, we can have None values, but for validated data, we should not have None values -> as part of ReadyDrone, we will validate and remove None values
    battery_level: int | None
    max_wind_speed: int | None


@dataclass(frozen=True)
class ReadyDrone: # Get this data based on telematry above. If anything is None, raise ValueError - Validated drone object here - so remove None conditions - fail fast if any of the required fields are None
    drone_id: str
    location: Coordinates
    battery_level: int
    max_wind_speed: int


@dataclass(frozen=True)
class Delivery:
    destination: Coordinates
    required_battery: int
    avoid_zones: list[GeoFence] = field(default_factory=list[GeoFence])


@dataclass(frozen=True)
class WeatherReport:
    wind_speed: int


class RouteRejected(Exception): # use this to raise error instead of returning None
    pass


class RouteDiagnostics(Protocol): # structural interface, "anything with a record(str) method."
    def record(self, message: str) -> None: ...


class ConsoleDiagnostics:
    def record(self, message: str) -> None:
        print(f"[diagnostics] {message}")


class NullDiagnostics:
    def record(self, message: str) -> None:
        pass


def prepare_drone(telemetry: DroneTelemetry) -> ReadyDrone:
    if telemetry.location is None:
        raise ValueError("Drone has no GPS location")

    if telemetry.battery_level is None:
        raise ValueError("Drone has no battery reading")

    if telemetry.max_wind_speed is None:
        raise ValueError("Drone has no wind safety rating")

    return ReadyDrone(
        drone_id=telemetry.drone_id,
        location=telemetry.location,
        battery_level=telemetry.battery_level,
        max_wind_speed=telemetry.max_wind_speed,
    )


def estimate_battery_usage(start: Coordinates, destination: Coordinates) -> int:
    return round(start.distance_to(destination) * 10)


def assign_delivery(
    drone: ReadyDrone,
    delivery: Delivery,
    weather: WeatherReport,
    diagnostics: RouteDiagnostics = NullDiagnostics(), # default instances share one object across all calls. Fine in this specific case; a thing to be aware of
) -> Route:
    diagnostics.record("Starting route assignment")

    if weather.wind_speed > drone.max_wind_speed:
        raise RouteRejected("Too windy for this drone")

    estimated_usage = estimate_battery_usage(
        drone.location,
        delivery.destination,
    )

    if drone.battery_level < estimated_usage:
        raise RouteRejected("Battery too low")

    diagnostics.record("Route assigned")

    return Route(
        start=drone.location,
        destination=delivery.destination,
        avoid_zones=delivery.avoid_zones,
    )


def main() -> None:
    #  The net effect: None handling is pushed to one boundary (prepare_drone), and the core business logic (assign_delivery) operates on types that are guaranteed valid, so it reads as a simple linear sequence of rules.   

    telemetry = DroneTelemetry(
        drone_id="drone-1",
        location=Coordinates(0, 0),
        battery_level=80,
        max_wind_speed=35,
    )

    drone = prepare_drone(telemetry) # get ready drone object with validated data - if any of the required fields are None, raise ValueError

    delivery = Delivery(
        destination=Coordinates(3, 4),
        required_battery=50,
        avoid_zones=[GeoFence("city-center")],
    )

    weather = WeatherReport(wind_speed=20)
    diagnostics = ConsoleDiagnostics()
   
    try:
        route = assign_delivery(drone, delivery, weather, diagnostics)
    except RouteRejected as error: # Instead of returning None, we raise an exception and handle it here
        print(f"No route could be assigned: {error}")
    else:
        print(route)


if __name__ == "__main__":
    main()