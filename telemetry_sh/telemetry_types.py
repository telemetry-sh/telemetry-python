from typing import Mapping, TypedDict, Literal, TypeVar, Generic
TelemetryQueryType = TypeVar("TelemetryQueryType", bound=Mapping)

class TelemetryQueryResponse(TypedDict, Generic[TelemetryQueryType]):
    data: list[TelemetryQueryType]
    status: Literal["success"]
    key_order: list[str]

class TelemetryLogResponse(TypedDict):
    status: Literal["success"]
    message: str

