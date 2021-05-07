# pylint: disable=invalid-name, no-self-use

"""Type Hint Remover based on AST"""

import ast


class TypeHintRemover(ast.NodeTransformer):

    """Type Hint Remover."""

    def __init__(self, custom_typing_module) -> None:
        super().__init__()
        self.custom_typing_module = custom_typing_module

    def visit_FunctionDef(self, node):
        """Remove the return type definition and all argument annotations"""

        node.returns = None
        if node.args.args:
            for arg in node.args.args:
                arg.annotation = None
        self.generic_visit(node)
        return node

    def visit_AnnAssign(self, node):
        """Remove types when in variable assigments"""
        if node.value is None:
            return None
        return ast.Assign([node.target], node.value)

    def visit_Import(self, node):
        """ Remove the `import typing` statements """
        node.names = [n for n in node.names if n.name != 'typing' and self.custom_typing_module not in n.name]
        return node if node.names else None

    def visit_ImportFrom(self, node):
        """ Remove the `from typing import X` statements """
        return None if node.module == 'typing' or (node.module and self.custom_typing_module in node.module) else node
