#!/usr/bin/env python3
"""New authentication class SessionDBAuth"""

from datetime import datetime, timedelta
from uuid import uuid4
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Authentication class SessionDBAuth"""
    def __init__(self):
        super().__init__()
        from models.user_session import UserSession
        UserSession()

    def create_session(self, user_id=None):
        """Create a new session and save it in the database."""
        if user_id is None or not isinstance(user_id, str):
            return None

        from models.user_session import UserSession

        user_session = UserSession(user_id=user_id, session_id=uuid4().hex)
        UserSession.load_from_file()
        user_session.save()
        return user_session.session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve the user ID based on a given session ID."""
        if session_id is None:
            return None
        from models.user_session import UserSession
        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions:
            return None
        if self.session_duration <= 0:
            return None
        created_at = user_sessions[0].created_at
        if created_at is None:
            return None
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None
        return user_sessions[0].user_id

    def destroy_session(self, request=None):
        """Delete a session from the database based on the request."""
        if request is None:
            return False

        session_id = self.session_cookie(request=request)
        if not session_id:
            return False

        from models.user_session import UserSession

        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions:
            return False
        user_sessions[0].remove()
        return True
