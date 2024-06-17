import datetime
from typing import List, Optional

from pydantic import BaseModel, field_validator

from domain.answer import answer_schema
from domain.user import user_schema


class Question(BaseModel):
    id: int
    title: str
    content: str
    created: datetime.datetime
    answers: List[answer_schema.Answer] = []  # 여기 이름은 모델의 backref와 일치시켜줘야 함
    user: Optional[user_schema.User]


class QuestionCreate(BaseModel):
    title: str
    content: str

    @field_validator("title", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: List[Question] = []
