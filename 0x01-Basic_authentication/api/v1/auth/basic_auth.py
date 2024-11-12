#!/usr/bin/env python3
"""
This module for BasicAuth
"""
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
