# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""
Core infrastructure components for the Dataverse SDK.

This module contains the foundational components including authentication,
configuration, HTTP client, and error handling.

Import classes directly from their specific modules:
    - Authentication: from .auth import AuthManager, TokenPair
    - Configuration: from .config import DataverseConfig  
    - Errors: from .errors import DataverseError, HttpError, etc.
    - HTTP Client: from .http import HttpClient
"""

# No re-exports to avoid documentation duplication with py2docfx
__all__ = []