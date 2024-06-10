from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal, get_db
from domain.question import question_crud, question_schema
from models import Question

router = APIRouter(
    prefix="/api/question",
)


# @router.get("/list")
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.created.desc()).all()
#     db.close()
#     return _question_list


# @router.get("/list")
# def question_list():
#     # with를 벗어나는 순간 get_db 함수의 finally에 작성한 db.close() 함수가 자동 실행될 것
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.created.desc()).all()
#     return _question_list


# get_db 함수를 with문과 함께 쓰는 대신에 question_list 함수의 매개변수로 객체를 주입받음
# db: Session 문장의 의미는 db 객체가 Session 타입임을 의미
# FastAPI의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다.
# 따라서 db: Session = Depends(get_db) 의 db 객체에는 get_db 제너레이터에 의해 생성된 세션 객체가 주입된다.
# 이 때, get_db 함수에 자동으로 contextmanager가 적용된다. -> database의 어노테이션 제거 필요
# @router.get(
#     "/list", response_model=List[question_schema.Question]
# )  # response_model=list[question_schema.Question]: question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미
# def question_list(db: Session = Depends(get_db)):
#     _question_list = db.query(Question).order_by(Question.created.desc()).all()
#     return _question_list


@router.get(
    "/list", response_model=question_schema.QuestionList
)  # response_model=list[question_schema.Question]: question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미
def question_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(db, skip=page * size, limit=size)
    return {"total": total, "question_list": _question_list}


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate, db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)
    return status.HTTP_201_CREATED
