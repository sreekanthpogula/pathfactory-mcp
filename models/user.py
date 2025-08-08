from pydantic import BaseModel

# Base user model without password
class User(BaseModel):
    username: str

# Model for storing hashed passwords (internal use)
class UserInDB(User):
    hashed_password: str
