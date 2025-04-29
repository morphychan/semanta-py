#!/usr/bin/env python3
"""
Semanta-py CLI Entrypoint

This script serves as the main entry point using the Semanta-py framework.

Usage:
    python3 -m scripts.analyze_project <project_path> [options]
"""

import argparse
from semanta import project_loader
from semanta.ast_parser import AstParser
from semanta.symbol_table import SymbolExtractor

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
        self.parser = AstParser()
        self.extractor = SymbolExtractor()

    def run(self):
        """
        Main execution method. Loads files, parses them, and performs analysis steps.
        """
        print(f"[INFO] Analyzing project at: {self.args.project_path}")
        print(f"[INFO] Options: dump_ast={self.args.dump_ast}, show_nodes={self.args.show_nodes}, limit={self.args.limit}")

        print("[STEP] Loading source files...")
        source_files = project_loader.load_sources(self.args.project_path)

        print("[STEP] Parsing files...")
        for i, (filename, source) in enumerate(source_files.items()):
            if self.args.limit is not None and i >= self.args.limit:
                break

            print(f" - Analyzing: {filename}")

            tree = self.parser.parse(source)
            if self.args.dump_ast:
                print("AST:", self.parser.dump(tree))

            if self.args.show_nodes:
                print("Top-level nodes:", self.parser.get_top_level_nodes(tree))

            if self.args.show_symbols:
                symbols = self.extractor.extract_symbols(tree)
                if not symbols:
                    print("[Symbols] (None found)")
                else:
                    print("[Symbols]")
                    self._pretty_print_symbols(symbols)

        print("[DONE] Analysis complete.")


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
            "--show-symbols",
            action="store_true",
            help="Display extracted symbols (functions, classes) for each file"
        )        
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Limit the number of files to process (useful for testing)"
        )
        return parser.parse_args()

    def _pretty_print_symbols(self, symbols):
        """
        Nicely print the extracted symbols in a structured way.

        Args:
            symbols (list[dict]): The extracted symbol information.
        """
        for sym in symbols:
            sym_type = sym.get("type", "Unknown")
            
            if sym_type == "FunctionDef":
                print(f"  - Function: {sym['name']} (line {sym['lineno']})")
                if sym.get("parameters"):
                    print(f"    Parameters: {', '.join(sym['parameters'])}")
                if sym.get("local_vars"):
                    print(f"    Local Variables: {', '.join(sym['local_vars'])}")
            
            elif sym_type == "ClassDef":
                print(f"  - Class: {sym['name']} (line {sym['lineno']})")
                if sym.get("methods"):
                    print(f"    Methods:")
                    for method in sym["methods"]:
                        print(f"      - {method['name']} (line {method['lineno']})")
                        if method.get("parameters"):
                            print(f"        Parameters: {', '.join(method['parameters'])}")
                        if method.get("local_vars"):
                            print(f"        Local Variables: {', '.join(method['local_vars'])}")
            
            elif sym_type == "Import":
                print(f"  - Import: {', '.join(sym['modules'])}")
            
            elif sym_type == "ImportFrom":
                print(f"  - From {sym['module']} import {', '.join(sym['imports'])}")
            
            else:
                print(f"  - Unknown symbol: {sym}")

if __name__ == "__main__":
    SemantaCLI().run()
