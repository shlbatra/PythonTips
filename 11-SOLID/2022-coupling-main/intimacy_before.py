"""
Avoid inappropriate intimacy
"""


from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Geolocation:
    id: int
    street: str
    postal_code: str
    city: str
    province: str
    latitude: float
    longitude: float


@dataclass
class Location:
    id: int
    message_id: str
    raw_data: str
    date: datetime
    priority: int
    #list of geolocations
    geolocation: list[Geolocation] = field(default_factory=list)

#access info about location depending on geolocation and other info you got
#higher coupling - depends on location and geolocation now
def generate_breadcrumbs(location: Location) -> dict[str, str]:
    breadcrumbs: dict[str, str] = {}
    main_url = "https://myapi.com"
    #only accessing geolocation first element here and not locatio
    if location.geolocation[0]:
        if location.geolocation[0].postal_code:
            breadcrumbs[
                "postal_code_url"
            ] = f"{main_url}/postal_code/{location.geolocation[0].postal_code}/"
        if location.geolocation[0].city:
            city_slug = location.geolocation[0].city.lower().replace(" ", "-")
            breadcrumbs["city_url"] = f"{main_url}/region/{city_slug}/"
        if location.geolocation[0].province:
            breadcrumbs[
                "province_url"
            ] = f"{main_url}/region/province/{location.geolocation[0].province.lower()}/"
    return breadcrumbs
