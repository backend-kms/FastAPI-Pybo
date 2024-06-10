# 모델로 데이터 처리하는 방법

"""
1. Question 모델 객체 생성
"""
# from datetime import datetime
# from models import Answer, Question
# q = Question(title="test_title_1", content="test_content_1", created=datetime.now())


"""
2. 객체 저장
- 객체를 만들었다고 해서 데이터가 저장되는 것은 아니다.
- 데이터베이스에 데이터를 저장하려면 database.py 파일의 SessionLocal 클래스로 생성한 db 세션 객체를 사용해야 한다.
- 신규 데이터를 저장할때는 db 객체의 add 함수를 사용한 다음 commit 함수까지 실행해야 한다.
- db 객체는 데이터베이스와 연결된 세션, 즉 접속된 상태를 의미한다.
- 데이터베이스를 처리하려면 이 세션이 필요하다.
- 세션을 통해 데이터를 저장, 수정, 삭제 작업을 한 다음에는 반드시 db.commit()으로 커밋을 해주어야 한다.
"""
# from database import SessionLocal

# db = SessionLocal()
# db.add(q)
# db.commit()

"""
3. 데이터가 잘 생성되었는지 확인
"""
# q.id

"""
4. 두번째 질문 데이터 생성
"""
# q = Question(title="test_title_2", content="test_content_2", created=datetime.now())
# db.add(q)
# db.commit()

"""
* 커밋(commit)과 롤백(rollback)
커밋은 취소할 수 없다. 그래서 수행한 작업을 취소하려면 커밋 이전에 진행해야 한다.
작업을 취소하고 싶으면 db.rollback()으로 되돌리기를 실행하면 된다.
"""

"""
5. 데이터 조회
like 함수에 전달한 문자열에 붙은 % 표기 (대소문자 구분하지 않으려면 ilike 사용)
- test%: test로 시작하는 문자열
- %test: test로 끝나는 문자열
- %test%: test를 포함하는 문자열
"""
# db.query(Question).all()
# db.query(Question).filter(Question.id==1).all()
# db.query(Question).get(1)
# db.query(Question).filter(Question.title.like('%1%')).all()

"""
6. 데이터 수정
"""
# q = db.query(Question).get(2)
# q.id
# q.title = "test_modify_title_1"
# db.commit()

"""
7. 데이터 삭제
"""
# q = db.query(Question).get(1)
# db.delete(q)
# db.commit()

"""
8. 답변 데이터 저장
"""
# >> q = db.query(Question).get(2)
# >> a = Answer(question=q, content="test_content_2", created=datetime.now())
# >> db.add(a)
# >> db.commit()
