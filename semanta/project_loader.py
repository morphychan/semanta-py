"""
project_loader.py

Recursively scan a directory for Python source files
and return their content as a dictionary of {relative_path: source_code}.
"""

import os

def load_sources(project_path):
    """
    Recursively load all .py source files in a project directory.

    Args:
        project_path (str): The root path of the Python project to analyze.

    Returns:
        dict[str, str]: A dictionary mapping file paths (relative to project root)
                        to their corresponding source code as strings.
    """
    source_files = {}

    for dirpath, dirnames, filenames in os.walk(project_path):
        for filename in filenames:
            if filename.endswith(".py"):
                abs_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(abs_path, start=project_path)

                try:
                    with open(abs_path, "r", encoding="utf-8") as f:
                        source = f.read()
                        source_files[rel_path] = source
                except (UnicodeDecodeError, OSError) as e:
                    print(f"[WARN] Skipped unreadable file: {abs_path} ({e})")

    return source_files
