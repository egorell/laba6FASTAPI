from pydantic import BaseModel
from typing import Optional

class InputGroup(BaseModel):
    name: str

class OutputGroup(BaseModel):
    id: int
    name: str
