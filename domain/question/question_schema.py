import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    title: str
    content: str
    created: datetime.datetime
