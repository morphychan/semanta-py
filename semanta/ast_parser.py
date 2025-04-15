"""
ast_parser.py

This module provides an interface for parsing Python source code
into abstract syntax trees (ASTs), dumping tree structure, 
and extracting structural information, etc.
"""

import ast

class AstParser:
    """
    A parser that wraps Python's built-in `ast` module for structured analysis.

    Supports parsing, dumping, and extracting high-level AST node information.
    """

    def __init__(self, mode: str = "exec"):
        """
        Initialize the parser with optional AST parsing mode.

        Args:
            mode (str): Mode passed to `ast.parse()`. Default is "exec".
                        Other options: "eval", "single" (for expressions or statements).
        """
        self.mode = mode

    def parse(self, source: str) -> ast.AST:
        """
        Parse Python source code into an AST tree.

        Args:
            source (str): The Python source code as a string.

        Returns:
            ast.AST: The parsed abstract syntax tree.
        """
        return ast.parse(source, mode=self.mode)

    def dump(self, tree: ast.AST, simplified: bool = True) -> str:
        """
        Dump the AST tree structure as a string (for debugging or inspection).

        Args:
            tree (ast.AST): The parsed AST.
            simplified (bool): If True, omit attributes and line numbers.

        Returns:
            str: Formatted string representation of the AST.
        """
        return ast.dump(tree, indent=4, annotate_fields=not simplified, include_attributes=not simplified)

    def get_top_level_nodes(self, tree: ast.AST) -> list[str]:
        """
        Extract the types of top-level AST nodes (e.g., FunctionDef, Import).

        Args:
            tree (ast.AST): The parsed AST.

        Returns:
            list[str]: List of top-level AST node type names.
        """
        if not isinstance(tree, ast.Module) or not hasattr(tree, "body"):
            return []

        return [type(node).__name__ for node in tree.body]
