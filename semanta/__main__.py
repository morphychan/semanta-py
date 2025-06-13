#!/usr/bin/env python3
"""
Semanta-py CLI Main Entry Point

This module serves as the main entry point for the semanta package when
executed with `python3 -m semanta`.

Usage:
    python3 -m semanta <command> [options]

Available commands:
    analyze    Analyze a Python project and extract semantic information
    help       Show help information
"""

import sys
import argparse
from .cli import SemantaCLI


def main():
    """
    Main entry point for the semanta CLI tool.
    """
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    # Create the main CLI controller
    cli = SemantaCLI()
    cli.run()


def print_usage():
    """Print basic usage information."""
    print("Semanta-py: Lightweight Python semantic analyzer")
    print()
    print("Usage:")
    print("    python3 -m semanta <command> [options]")
    print()
    print("Available commands:")
    print("    analyze    Analyze a Python project and extract semantic information")
    print("    help       Show help information")
    print()
    print("Use 'python3 -m semanta <command> --help' for more information on a command.")


if __name__ == "__main__":
    main() 
