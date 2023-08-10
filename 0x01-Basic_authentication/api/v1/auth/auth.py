#!/usr/bin/env python3
"""Authentication module for the API.
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for the given path.
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """Gets the authorization header field from the request.
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from the request.
        """
        return None