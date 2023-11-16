from pydantic import BaseModel


class AuthorizationInput(BaseModel):
    hostname: str
    branch: int
    email: str
    api_key: str
    auth_result: dict


class CustomerParameters(BaseModel):
    id: int
    is_study: int
    name: str
    lead_status_id: int
    page: int


class CustomerCreateParameters(BaseModel):
    is_study: int
    name: str
    legal_type: bool
