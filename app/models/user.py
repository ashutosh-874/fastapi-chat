from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.session import Base  # Import the Base from base.py

class User(Base):
    __tablename__ = "users"

    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Unique ID
    username            = Column(String, unique=True, nullable=False)  # Unique username
    first_name          = Column(String, nullable=False)
    last_name           = Column(String, nullable=False)
    profile_picture     = Column(String, nullable=True)  # URL or path to the profile picture

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, first_name={self.first_name}, last_name={self.last_name})>"
