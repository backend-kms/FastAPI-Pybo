import contextlib

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_pybo_project_1.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
Base.metadata = MetaData(naming_convention=naming_convention)

# db 세션 객체를 리턴하는 제너레이터인 get_db 함수 추가, @contextlib.contextmanager 어노테이션 적용했으므로 with 문과 함께 사용 가능
# @contextlib.contextmanager
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Depends 사용시 어노테이션 제거 필요
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
