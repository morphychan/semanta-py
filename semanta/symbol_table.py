"""
symbol_table.py

This module provides functionality to extract basic symbol information
(functions, classes) from a Python AST.
"""

import ast
from typing import List, Dict

class SymbolExtractor:
    """
    Extracts top-level function and class definitions from an AST tree.
    """

    def __init__(self):
        """
        Initialize the symbol extractor. Reserved for future configuration options.
        """
        pass

    def extract_symbols(self, tree: ast.AST) -> List[Dict[str, object]]:
        """
        Extract symbols from the given AST.

        Args:
            tree (ast.AST): The abstract syntax tree to analyze.

        Returns:
            List[Dict[str, object]]: A list of dictionaries, each representing a symbol with
            its name, type, and line number.
        """
        symbols = []

        if not isinstance(tree, ast.Module) or not hasattr(tree, "body"):
            return symbols  # Return empty if tree structure is unexpected

        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                symbol_info = {
                    "name": node.name,
                    "type": type(node).__name__,
                    "lineno": getattr(node, "lineno", -1),
                }
                symbols.append(symbol_info)

        return symbols