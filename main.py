from fastapi import FastAPI

# FastAPI의 핵심 객체
app = FastAPI()


# hello라는 URL 요청이 발생하면 해당 함수를 실행해 결과를 리턴하라는 어노테이션
@app.get("/hello")
def Hello():
    return {"message": "안녕하세요."}
