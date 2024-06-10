import datetime

from pydantic import BaseModel, field_validator


# 답변 등록 시 사용할 스키마
# content는 필숫값이긴 하지만 ""처럼 빈 문자열이 입력 가능해야 함
class AnswerCreate(BaseModel):
    content: str

    # @field_validator('content') 어노테이션을 적용한 not_empty 함수 추가
    # not_empty 함수는 AnswerCreate 스키마에 content 값이 저장될 때 실행됨
    @field_validator("content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


# 질문 상세 조회에 사용할 Answer 스키마, 답변 1건
class Answer(BaseModel):
    id: int
    content: str
    created: datetime.datetime
