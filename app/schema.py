from typing import Literal
from pydantic import BaseModel


class ClassifierResult(BaseModel):
    reasoning: str
    category: Literal["fraud", "card", "transfer", "app_access", "other"]
    urgency: Literal["critical", "high", "medium", "low"]
