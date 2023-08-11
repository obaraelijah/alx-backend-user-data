#!/usr/bin/env python3
"""Basic authentication module the API.
"""
import base64
from .auth import Auth

class BasicAuth(Auth):
    """Basic authentication class.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header for a Basic Authentication.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        token = authorization_header.split(' ')[-1]
        return token
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes a base64-encoded authorization header.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            res = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(res)
            return decoded.decode('utf-8')
        except  base64.binascii.Error:
            return None
