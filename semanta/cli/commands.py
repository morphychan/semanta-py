"""
Semanta CLI Commands

This module contains the implementation of individual CLI commands.
Each command is implemented as a separate class for better organization.
"""

from .. import project_loader
from ..ast_parser import AstParser
from ..symbol_table import SymbolExtractor

class AnalyzeCommand:
    """Command handler for the 'analyze' subcommand."""
    
    def __init__(self):
        """Initialize the analyze command."""
        self.symbol_extractor = SymbolExtractor()
    
    def execute(self, args):
        """
        Execute the analyze command.
        
        Args:
            args: Parsed command line arguments
        """
        print(f"[INFO] Analyzing project at: {args.project_path}")
        print(f"[INFO] Options: dump_ast={args.dump_ast}, show_nodes={args.show_nodes}, show_symbols={args.show_symbols}, limit={args.limit}")

        print("[STEP] Loading source files...")
        source_files = project_loader.load_sources(args.project_path)
        
        if not source_files:
            print("[WARN] No Python files found in the specified directory.")
            return

        print(f"[INFO] Found {len(source_files)} Python files")
        print("[STEP] Parsing files...")
        
        parser = AstParser()
        processed_count = 0
        
        for filename, source in source_files.items():
            if args.limit is not None and processed_count >= args.limit:
                break

            print(f" - Analyzing: {filename}")

            try:
                tree = parser.parse(source)
                
                if args.dump_ast:
                    print(f"   AST for {filename}:")
                    print(f"   {parser.dump(tree)}")
                    print()

                if args.show_nodes:
                    nodes = parser.get_top_level_nodes(tree)
                    print(f"   Top-level nodes: {nodes}")

                if args.show_symbols:
                    symbols = self.symbol_extractor.extract_symbols(tree)
                    if not symbols:
                        print("   [Symbols] (None found)")
                    else:
                        print("   [Symbols]")
                        self.symbol_extractor.pretty_print_symbols(symbols, indent="     ")
                    
                processed_count += 1
                
            except SyntaxError as e:
                print(f"   [ERROR] Syntax error in {filename}: {e}")
            except Exception as e:
                print(f"   [ERROR] Failed to process {filename}: {e}")

        print(f"[DONE] Analysis complete. Processed {processed_count} files.")

class HelpCommand:
    """Command handler for the 'help' subcommand."""
    
    def __init__(self, parser):
        """
        Initialize the help command.
        
        Args:
            parser: The main argument parser
        """
        self.parser = parser
    
    def execute(self, args):
        """
        Execute the help command.
        
        Args:
            args: Parsed command line arguments
        """
        if args.subcommand:
            # Show help for specific subcommand
            try:
                self.parser.parse_args([args.subcommand, "--help"])
            except SystemExit:
                pass  # argparse calls sys.exit after showing help
        else:
            # Show general help
            self.parser.print_help() 