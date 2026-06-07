"""Narratological Analysis Protocols.

Defines the P1-P7 protocol framework for analyzing creative works.
"""

from narratological.models.protocol import ProtocolLevel, ProtocolSpec
from narratological.protocols.registry import PROTOCOLS, get_protocol

__all__ = [
    "ProtocolLevel",
    "ProtocolSpec",
    "PROTOCOLS",
    "get_protocol",
]
