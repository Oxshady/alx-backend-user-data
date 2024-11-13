#!/usr/bin/env python3
"""Session Authentication"""
from uuid import uuid4
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth that inherit from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create in memory session for the user"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = uuid4().hex
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id
