#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]):
        """require authentication"""
        pass

    def authorization_header(self, request=None):
        """authorization header"""
        pass

    def current_user(self, request=None):
        """current user"""
        pass
