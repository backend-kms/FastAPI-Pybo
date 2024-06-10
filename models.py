from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    # __tablename__: 모델에 의해 관리되는 Table의 이름
    __tablename__ = "question"

    # 디폴트 nullable=True
    id = Column(Integer, primary_key=True)  # 고유 번호
    title = Column(String, nullable=False)  # 질문 제목, 필수
    content = Column(Text, nullable=False)  # 질문 내용, 필수
    created = Column(DateTime, nullable=False)  # 작성일시, 필수


# from sqlalchemy.sql import func
# , server_default=func.now()


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)  # 고유 번호
    content = Column(Text, nullable=False)  # 답변 내용
    created = Column(DateTime, nullable=False)  # 작성일시, 필수
    question_id = Column(Integer, ForeignKey("question.id"))  # 질문의 id
    question = relationship(
        "Question", backref="answers"
    )  # Answer 모델에서 Question모델을 참조하기 위한 속성 relationship(참조할 속성, 역참조할 속성)
