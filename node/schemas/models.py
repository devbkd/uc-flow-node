from pydantic import BaseModel


class EmailInput(BaseModel):
    email_input: str


class DatetimeInput(BaseModel):
    datetime_input: str
