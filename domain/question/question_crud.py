import datetime

from sqlalchemy.orm import Session

from domain.question import question_schema
from models import Question, User


def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question).order_by(Question.created.desc())
    total = _question_list.count()
    # skip: 조회한 데이터의 시작 위치, limit: 시작 위치부터 가져올 데이터의 건수
    # ex) 300 개의 데이터 중 21~30번째 데이터를 가져오려면 skip:20, limit:10
    question_list = (
        _question_list.offset(skip).limit(limit).all()
    )  # 전체 건수, 페이징 적용될 질문 목록
    return total, question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question


def create_question(db: Session, question_create: question_schema.QuestionCreate, user: User):
    db_question = Question(
        title=question_create.title,
        content=question_create.content,
        created=datetime.datetime.now(),
        user=user,
    )
    db.add(db_question)
    db.commit()


def update_question(
    db: Session, db_question: Question, question_update: question_schema.QuestionUpdate
):
    db_question.title = question_update.title
    db_question.content = question_update.content
    db_question.updated = datetime.datetime.now()
    db.add(db_question)
    db.commit()
