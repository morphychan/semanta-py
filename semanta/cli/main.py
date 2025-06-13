#!/usr/bin/env python3
"""
Semanta CLI Main Controller

This module provides the main command-line interface controller for semanta,
supporting multiple subcommands for different analysis operations.
"""

import argparse
import sys
from .commands import AnalyzeCommand, HelpCommand


class SemantaCLI:
    """
    Command-line interface controller for Semanta-py.
    Handles argument parsing, subcommand routing, and execution.
    """

    def __init__(self):
        """
        Initialize the CLI tool by setting up the argument parser and commands.
        """
        self.parser = self._create_parser()
        self.commands = self._setup_commands()

    def _create_parser(self):
        """
        Create the main argument parser with subcommands.

        Returns:
            argparse.ArgumentParser: Configured argument parser.
        """
        parser = argparse.ArgumentParser(
            prog="semanta",
            description="Semanta-py: Lightweight Python semantic analyzer"
        )
        
        subparsers = parser.add_subparsers(
            dest="command",
            help="Available commands",
            metavar="<command>",
            required=True
        )

        # Add analyze subcommand
        self._add_analyze_command(subparsers)
        
        # Add help subcommand
        self._add_help_command(subparsers)

        return parser

    def _setup_commands(self):
        """
        Initialize command handlers.
        
        Returns:
            dict: Command name to handler mapping
        """
        return {
            "analyze": AnalyzeCommand(),
            "help": HelpCommand(self.parser)
        }

    def _add_analyze_command(self, subparsers):
        """Add the 'analyze' subcommand."""
        analyze_parser = subparsers.add_parser(
            "analyze",
            help="Analyze a Python project and extract semantic information"
        )
        analyze_parser.add_argument(
            "project_path",
            help="Path to the Python project directory to analyze"
        )
        analyze_parser.add_argument(
            "--dump-ast",
            action="store_true",
            help="Print raw AST using ast.dump() for each file"
        )
        analyze_parser.add_argument(
            "--show-nodes",
            action="store_true",
            help="Display top-level AST node types for each file"
        )
        analyze_parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Limit the number of files to process (useful for testing)"
        )

    def _add_help_command(self, subparsers):
        """Add the 'help' subcommand."""
        help_parser = subparsers.add_parser(
            "help",
            help="Show help information"
        )
        help_parser.add_argument(
            "subcommand",
            nargs="?",
            help="Show help for a specific subcommand"
        )

    def run(self):
        """
        Main execution method. Parses arguments and routes to appropriate handler.
        """
        args = self.parser.parse_args()
        
        # Execute the appropriate command
        if args.command in self.commands:
            self.commands[args.command].execute(args)
        else:
            self.parser.print_help()
            sys.exit(1) 