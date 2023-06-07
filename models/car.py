from pydantic import BaseModel

class Car(BaseModel):
    maker: str
    model: str