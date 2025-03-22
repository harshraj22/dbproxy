import uuid
from pydantic import BaseModel, Field

class Profile(BaseModel):
    name: str
    email: str
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }
        
    @classmethod
    def create(cls, name: str, email: str):
        """Factory method to create a new profile"""
        return cls(name=name, email=email)