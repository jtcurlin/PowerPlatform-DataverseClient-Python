# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""
Data access layer for the Dataverse SDK.

This module contains OData protocol handling, CRUD operations, metadata management,
SQL query functionality, and file upload capabilities.

Import classes directly from their specific modules:
    - OData operations: from .odata import ODataClient
    - File uploads: from .upload import ODataFileUpload
"""

# No re-exports to avoid documentation duplication with py2docfx
__all__ = []