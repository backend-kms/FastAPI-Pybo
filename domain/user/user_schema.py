from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core.core_schema import FieldValidationInfo


class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr
    # EmailStr: 해당 값이 이메일 형식과 일치하는지 검증하기 위해 사용
    # EmailStr을 사용하기 위해 email_validator 설치 필요
    # pip install "pydantic[email]"

    @field_validator("username", "password1", "password2", "email")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

    # 입력항목인 password1과 password2가 동일한지 검증
    # passwords_match 메서드의 info 매개변수의 info.data에는 UserCreate의 속성들이 {변수명: 값, ...} 형태로 전달됨
    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v
