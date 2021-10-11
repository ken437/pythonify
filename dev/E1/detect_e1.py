import ast

"""
Determine if an AST subscript object is an E1 antipattern
@param subscript: (ast.Subscript) the object to check
"""
def subscript_is_e1(subscript):
    # Remember, E1 looks like a[len(a) - #]
    if isinstance(subscript.value, ast.Name):
        varname_idxed = subscript.value.id
    else:
        return False

    if isinstance(subscript.slice, ast.BinOp) and isinstance(subscript.slice.op, ast.Sub) and isinstance(subscript.slice.right, ast.Constant):
        if isinstance(subscript.slice.left, ast.Call):
            if isinstance(subscript.slice.left.func, ast.Name) and subscript.slice.left.func.id == "len":
                func_args = subscript.slice.left.args
                if len(func_args) == 1 and isinstance(func_args[0], ast.Name):
                    if func_args[0].id == varname_idxed:
                        if isinstance(subscript.slice.right.value, int):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

"""
Determine if an AST object contains an E1 antipattern
@param in_ast: (ast.AST) the AST object to search recursively
"""
def ast_has_e1(in_ast):
    assert(isinstance(in_ast, ast.AST))

    # First check if this is an E1
    if isinstance(in_ast, ast.Subscript):
        if subscript_is_e1(in_ast):
            return True

    # If this isn't an E1, maybe it contains an E1
    for fieldname in in_ast._fields:
        field = getattr(in_ast, fieldname)
        if isinstance(field, list):
            for field_entry in field:
                if isinstance(field_entry, ast.AST) and ast_has_e1(field_entry):
                    return True
        else:
            if isinstance(field, ast.AST) and ast_has_e1(field):
                return True
    return False


"""
Determine whether a file contains the E1 (access from end of list without negative index)
antipattern
@param file_contents: (str) text of Python file
@return: (bool) true iff the E1 antipattern is present
"""
def has_e1(file_contents):
    ast_contents = ast.parse(file_contents)
    # print(file_contents)
    # print(ast.dump(ast_contents))
    return ast_has_e1(ast_contents)
