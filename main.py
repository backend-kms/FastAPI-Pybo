from fastapi import FastAPI

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

# FastAPI의 핵심 객체
app = FastAPI()

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)


# hello라는 URL 요청이 발생하면 해당 함수를 실행해 결과를 리턴하라는 어노테이션
# @app.get("/hello")
# def Hello():
#     return {"message": "안녕하세요."}
