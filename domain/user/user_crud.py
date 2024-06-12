from passlib.context import CryptContext
from sqlalchemy.orm import Session

from domain.user import user_schema
from models import User

# bcrypt 알고리즘을 사용하는 pwd_context 객체를 생성하고 pws_context 객체를 사용하여 비밀번호를 암호화하여 저장
# 이후 로그인시 사용자로부터 입력받은 비밀번호를 동일한 방식으로 암호화한 후 데이터베이스에 저장된 값과 비교하여 비밀번호가 동일한지 체크 가능
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user_create: user_schema.UserCreate):
    db_user = User(
        username=user_create.username,
        password=pwd_context.hash(user_create.password1),
        email=user_create.email,
    )
    # 비밀번호는 복호화할 수 없는 값으로 암호화해서 저장 필요 -> passlib 필요
    # pip install "passlib[bcrypt]"
    db.add(db_user)
    db.commit()


# 동일한 username | email로 등록된 사용자가 있는지 조회하는 쿼리 함수
def get_existing_user(db: Session, user_create: user_schema.UserCreate):
    return (
        db.query(User)
        .filter((User.username == user_create.username) | (User.email == user_create.email))
        .first()
    )
