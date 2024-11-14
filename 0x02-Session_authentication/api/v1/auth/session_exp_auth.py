#!/usr/bin/env python3
"""Session with expiration data"""
from os import getenv
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session with expiration data"""
    def __init__(self):
        super().__init__()
        try:
            self.session_duration = int(getenv("SESSION_DURATION", "0"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Overload create session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overload user id for session id"""
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict['user_id']

        created_at = session_dict.get('created_at')
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None

        return session_dict['user_id']
