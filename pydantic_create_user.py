from pydantic import BaseModel, EmailStr, Field, UUID4


class UserSchema(BaseModel):
    """
    Структура данных пользователя.
    """
    id: UUID4
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных запроса на создание пользователя.
    """
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Структура данных ответа на создание пользователя.
    """
    user: UserSchema
