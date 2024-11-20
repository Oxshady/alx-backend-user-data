#!/usr/bin/env python3
"""
This module defines the User model for a database using SQLAlchemy
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base


base = declarative_base()


class User(base):
    """
    User: Represents a user with fields for ID, email,
    hashed password, and session ID.
    """
    __tablename__ = 'users'

    id = Column(String(255), primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
