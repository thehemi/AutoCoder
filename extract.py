import re
import ast
import astor

"""
This function extracts function declarations and their bodies tabbed from the given source string. It returns the modified source string with function bodies removed and a dictionary containing function names as keys and their respective headers and bodies as values.

:param source: The source string containing function declarations and their bodies.
:return: A tuple containing the modified source string with function bodies removed and a dictionary with function names as keys and their headers and bodies as values.
"""
def extract_functions_python(source):
    parsed = ast.parse(source)
    functions = {}
    remaining_nodes = []

    for node in parsed.body:
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            function_header = astor.to_source(node.args)
            function_body = astor.to_source(node.body)
            functions[function_name] = {
                "header": function_header,
                "body": function_body.strip()
            }
        else:
            remaining_nodes.append(node)

    remaining_source = astor.to_source(ast.Module(body=remaining_nodes)).strip()
    return functions, remaining_source

"""
This function extracts function declarations and their bodies enclosed in braces from the given source string. It returns the modified source string with function bodies removed and a dictionary containing function names as keys and their respective headers and bodies as values.

:param source: The source string containing function declarations and their bodies.
:return: A tuple containing the modified source string with function bodies removed and a dictionary with function names as keys and their headers and bodies as values.
"""
def extract_functions_braces(source: str):
    function_pattern = r'(\w+\s+\w+\s*\([^()]*\)\s*{(?:[^{}]*|{[^{}]*})*})'
    function_bodies = {}
    matches = re.finditer(function_pattern, source, re.MULTILINE)

    for match in matches:
        function_str = match.group(1)
        signature, body = function_str.split('{', 1)
        body = '{' + body
        name = re.search(r'\w+\s+(\w+)\s*\(', signature).group(1)
        function_bodies[name] = {'header': signature, 'body': body}

        # Replace function body with an empty string
        source = source.replace(function_str, '')

    return source, function_bodies