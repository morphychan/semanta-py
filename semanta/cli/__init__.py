"""
Semanta CLI Package

This package contains all command-line interface related functionality
for the semanta static analysis tool.

The package is organized as follows:
    main.py: Main CLI controller and argument parsing
    commands.py: Individual command implementations
"""

from .main import SemantaCLI
from .commands import AnalyzeCommand, HelpCommand

__all__ = [
    "SemantaCLI",
    "AnalyzeCommand", 
    "HelpCommand"
] 