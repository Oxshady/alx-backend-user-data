#!/usr/bin/env python3
"""
This module for BasicAuth
"""
from typing import TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth and serves as a
    placeholder for basic
    authentication features to be expanded in the future.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the
        Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        from base64 import b64decode
        from binascii import Error

        try:
            from_b64 = b64decode(base64_authorization_header)
            return from_b64.decode("UTF-8")
        except Error as err:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        returns the user email and password from
        the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if decoded_base64_authorization_header.find(":") == -1:
            return (None, None)
        return tuple(decoded_base64_authorization_header.strip().split(":"))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """get user object from credential"""
        if not isinstance(user_email, str):
            return None
        if not isinstance(user_pwd, str):
            return None
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        from models.user import User

        User.load_from_file()
        users = User.search({"email": user_email})
        if not users:
            return None
        if not users[0].is_valid_password(user_pwd):
            return None
        return users[0]

    def current_user(self, request=None) -> TypeVar("User"):
        """complete authentication"""
        token = self.authorization_header(request=request)
        if token is not None:
            token = self.extract_base64_authorization_header(token)
            if token is not None:
                token = self.decode_base64_authorization_header(token)
                if token is not None:
                    token = self.extract_user_credentials(token)
                    if token is not None:
                        user = self.user_object_from_credentials(token[0], [1])
                        return user
        return None
