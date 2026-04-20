from pydantic import BaseModel

class NotificationCreate(BaseModel):
    title: str
    message: str
    status: str

class NotificationResponse(BaseModel):
    id: str
    title: str
    message: str
    status: str
