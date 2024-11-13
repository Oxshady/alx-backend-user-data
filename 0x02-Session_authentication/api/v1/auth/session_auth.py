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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return user_if of user that have the session"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """get a User based on his session ID"""
        cookie = self.session_cookie(request=request)
        if cookie:
            user_id = self.user_id_for_session_id(cookie)
            if user_id:
                from models.user import User
                return User.get(user_id)
