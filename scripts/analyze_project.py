#!/usr/bin/env python3
"""
Semanta-py CLI Entrypoint

This script serves as the main entry point using the Semanta-py framework.

Usage:
    python3 scripts/analyze_project.py <project_path> [options]
"""

import argparse

class SemantaCLI:
    """
    Command-line interface controller for Semanta-py.
    Handles argument parsing, file loading, and dispatching analysis steps.
    """

    def __init__(self):
        """
        Initialize the CLI tool by parsing arguments and preparing state.
        """
        self.args = self._parse_args()

    def _parse_args(self):
        """
        Define and parse CLI arguments using argparse.

        Returns:
            argparse.Namespace: Parsed command-line arguments.
        """
        parser = argparse.ArgumentParser(
            description="Semanta-py: Lightweight Python semantic analyzer"
        )
        parser.add_argument(
            "project_path",
            help="Path to the Python project directory to analyze"
        )
        parser.add_argument(
            "--dump-ast",
            action="store_true",
            help="Print raw AST using ast.dump() for each file"
        )
        parser.add_argument(
            "--show-nodes",
            action="store_true",
            help="Display top-level AST node types for each file"
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Limit the number of files to process (useful for testing)"
        )
        return parser.parse_args()

    def run(self):
        """
        Main execution method. Loads files, parses them, and performs analysis steps.
        """
        print(f"[INFO] Analyzing project at: {self.args.project_path}")
        print(f"[INFO] Options: dump_ast={self.args.dump_ast}, show_nodes={self.args.show_nodes}, limit={self.args.limit}")

        print("[STEP] Loading source files...")
        # Placeholder: Replace with project_loader.load_sources()
        source_files = {
            "mock_file.py": "def foo():\n    return 1"
        }

        print("[STEP] Parsing files...")
        for i, (filename, source) in enumerate(source_files.items()):
            if self.args.limit is not None and i >= self.args.limit:
                break

            print(f" - Analyzing: {filename}")

            # Placeholder: Replace with ast_parser.parse(source)
            if self.args.dump_ast:
                print("   [AST] <ast.dump(...) output here>")

            if self.args.show_nodes:
                print("   [Nodes] <top-level AST node types here>")

        print("[DONE] Analysis complete.")

if __name__ == "__main__":
    SemantaCLI().run()
