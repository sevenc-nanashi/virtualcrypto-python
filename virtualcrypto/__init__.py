"""Top-level package for VirtualCrypto.py."""
from .structs import User, Currency, Claim, ClaimStatus, Scope
from .errors import VirtualCryptoException, MissingScope
from .client import VirtualCryptoClient
from .async_client import AsyncVirtualCryptoClient

__author__ = """sizumita"""
__email__ = 'contact@sumidora.com'
__version__ = '0.1.1'
