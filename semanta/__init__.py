"""
Semanta-py: Lightweight Python Static Analysis Framework

This package provides tools for parsing and analyzing Python source code
using abstract syntax trees (ASTs) to extract semantic information.

Main modules:
    ast_parser: Core AST parsing functionality
    project_loader: File loading and project scanning utilities
    cli: Command-line interface for the semanta tool
"""

from .ast_parser import AstParser
from .project_loader import load_sources

__version__ = "0.1.0"
__author__ = "Semanta-py Project"

__all__ = [
    "AstParser",
    "load_sources",
] 