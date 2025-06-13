"""
Semanta CLI Commands

This module contains the implementation of individual CLI commands.
Each command is implemented as a separate class for better organization.
"""

from .. import project_loader
from ..ast_parser import AstParser


class AnalyzeCommand:
    """Command handler for the 'analyze' subcommand."""
    
    def __init__(self):
        """Initialize the analyze command."""
        pass
    
    def execute(self, args):
        """
        Execute the analyze command.
        
        Args:
            args: Parsed command line arguments
        """
        print(f"[INFO] Analyzing project at: {args.project_path}")
        print(f"[INFO] Options: dump_ast={args.dump_ast}, show_nodes={args.show_nodes}, limit={args.limit}")

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