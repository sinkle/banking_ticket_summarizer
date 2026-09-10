from pydantic import BaseModel


class ClassifierResult(BaseModel):
    note: str
    category: str
    urgency: str
