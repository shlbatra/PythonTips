# How to avoid None checks

1. Use better defaults
2. Do validation sooner -> raw data adheres to constraints and fail fast
3. Rely on exceptions -> when return type from method has an option for None ex. int | None
4. Be explicit about modeling states ex. ReadyDrone (strict state of DroneTelematory) - extend to OfflineDrone, ConnectedDrone and then pass particular state toe particular logic - try valid defined states and have less occurances of invalid states not defined
5. Use NULL object pattern -> Doing nothing is a valid operation, Ex. RouteDiagnostics -> have NullDiagnostics do nothing use in place of None
6. Sentinel object -> Null valid then another value for not provided. Define special object. Ex. MISSING = object() -> this represent missing value, in api - caller passing None vs no value passed
7. Result Object -> return result indicating something has been rejected or failed. type RouteResult = Route | RouteFailed, RouteFailed class -> defined seperately - used in functional programming or rust. Python -> returns package. In python, exceptions preferred instead of returns.

Defensive programming - useful at edges ex. Raw data from drone or API retrieval. Inside domain core, need to be really strict. ReadyDrone strict vs DroneTelematory - get raw data can be invalid, 
Separating raw and messy data at edge and clean / strict data use in core logic.
