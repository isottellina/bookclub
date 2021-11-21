import uuid

import bcrypt
import sqlalchemy as sa
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    username = sa.Column(sa.String(50), nullable=False)
    _password = sa.Column('password', sa.String(60), nullable=False)
    is_admin = sa.Column(sa.Boolean(), default=False, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_value):
        if isinstance(new_value, str):
            new_value = new_value.encode()

        self._password = bcrypt.hashpw(new_value, bcrypt.gensalt())

    def checkpw(self, password):
        return bcrypt.checkpw(password, self._password)

class Tag(Base):
    __tablename__ = "tags"

    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)


class Book(Base):
    __tablename__ = "books"

    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = sa.Column(sa.String(150), nullable=False)
    description = sa.Column(sa.Text(), nullable=False)


class BookTags(Base):
    __tablename__ = "book_tags"

    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    book_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('books.id', ondelete="CASCADE"))
    tag_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('tags.id', ondelete="CASCADE"))
