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
            if isinstance(node, ast.FunctionDef):
                symbols.append(self._extract_function_symbols(node))
            elif isinstance(node, ast.ClassDef):
                symbols.append(self._extract_class_symbols(node))
            elif isinstance(node, ast.Import):
                symbols.append(self._extract_import_symbols(node))
            elif isinstance(node, ast.ImportFrom):
                symbols.append(self._extract_import_from_symbols(node))
        return symbols

    def _extract_function_symbols(self, node: ast.FunctionDef) -> Dict[str, object]:
        """
        Extracts symbols from a function definition.

        Args:
            node (ast.FunctionDef): The function definition node.

        Returns:
            Dict[str, object]: A dictionary with function's name, type, line number,
            and its parameters.
        """
        function_info = {
            "name": node.name,
            "type": "FunctionDef",
            "lineno": node.lineno,
            "parameters": [arg.arg for arg in node.args.args]
        }

        # Extract local variables (in case of assignment in function body)
        local_vars = self._extract_local_variables(node)
        function_info["local_vars"] = local_vars

        return function_info

    def _extract_class_symbols(self, node: ast.ClassDef) -> Dict[str, object]:
        """
        Extracts symbols from a class definition.

        Args:
            node (ast.ClassDef): The class definition node.

        Returns:
            Dict[str, object]: A dictionary with class's name, type, line number,
            and its methods.
        """
        class_info = {
            "name": node.name,
            "type": "ClassDef",
            "lineno": node.lineno,
            "methods": []
        }

        # Extract methods inside the class
        for sub_node in node.body:
            if isinstance(sub_node, ast.FunctionDef):
                method_info = self._extract_function_symbols(sub_node)
                class_info["methods"].append(method_info)

        return class_info

    def _extract_local_variables(self, node: ast.FunctionDef) -> List[str]:
        """
        Extracts local variables defined within a function (using assignment).

        Args:
            node (ast.FunctionDef): The function definition node.

        Returns:
            List[str]: A list of local variable names.
        """
        local_vars = []
        for sub_node in node.body:
            if isinstance(sub_node, ast.Assign):
                for target in sub_node.targets:
                    if isinstance(target, ast.Name):
                        local_vars.append(target.id)
        return local_vars

    def _extract_import_symbols(self, node: ast.Import) -> Dict[str, object]:
        """
        Extracts symbols from an import statement.

        Args:
            node (ast.Import): The import statement node.

        Returns:
            Dict[str, object]: A dictionary with the imported modules.
        """
        imports = []
        for alias in node.names:
            imports.append(alias.name)
        return {
            "type": "Import",
            "modules": imports
        }

    def _extract_import_from_symbols(self, node: ast.ImportFrom) -> Dict[str, object]:
        """
        Extracts symbols from a `from ... import ...` statement.

        Args:
            node (ast.ImportFrom): The `from ... import ...` statement node.

        Returns:
            Dict[str, object]: A dictionary with the imported modules or names.
        """
        imports = []
        for alias in node.names:
            imports.append(alias.name)
        return {
            "type": "ImportFrom",
            "module": node.module,
            "imports": imports
        }