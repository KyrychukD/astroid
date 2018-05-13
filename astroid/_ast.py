import sys

import typed_ast.ast3 as _ast_py3
import typed_ast.ast27 as _ast_py2


PYTHON_3 = 3
PYTHON_2 = 2


def _parse(string, python_version: int = PYTHON_3):
    parser_version = sys.version_info[1]
    if python_version == PYTHON_2:
        _ast = _ast_py2
    else:
        _ast = _ast_py3
    return _ast.parse(string, feature_version=parser_version)
