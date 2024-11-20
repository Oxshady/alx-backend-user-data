#!/usr/bin/env python3
"""
This module defines the User model for a database using SQLAlchemy
"""
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


base = declarative_base()


class User(base):
    """
    User: Represents a user with fields for ID, email,
    hashed password, and session ID.
    """
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    session_id: Mapped[str] = mapped_column(String(255), nullable=True)
