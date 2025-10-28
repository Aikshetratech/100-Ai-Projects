import ast
import re

def extract_python_doc(file_path):
    """
    Extracts docstrings and comments from a Python file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    # Extract docstrings using AST
    docstrings = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            doc = ast.get_docstring(node)
            if doc:
                docstrings.append(doc)

    # Extract comments using regex and clean '#' symbol
    comments = [re.sub(r"^#\s*", "", c) for c in re.findall(r"#.*", source)]

    return "\n".join(docstrings + comments)
