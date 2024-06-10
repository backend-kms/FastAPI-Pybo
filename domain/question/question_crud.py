from sqlalchemy.orm import Session

from models import Question


def get_question_list(db: Session):
    question_list = db.query(Question).order_by(Question.created.desc()).all()
    return question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question
