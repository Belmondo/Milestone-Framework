from pydantic import BaseModel, Field
from typing import Optional

class InstanceIDResponse(BaseModel):
    instance_id: str

class Neural_Network_Response(BaseModel):
    comando: str

class Data(BaseModel):
    # 3 entradas (floats) exigidas pelo monitoramento
    time_behaviour: Optional[float] = Field(None, description="Time behaviour (e.g., response time)")
    resource:       Optional[float] = Field(None, description="Resource utilization")
    capacity:       Optional[float] = Field(None, description="Capacity")