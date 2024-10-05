"""
    FeatureProof Middleware: FolderInfo.py

    Initialize and provide access to the func_dir object for folder operations.
"""
import ida_dirtree

# Initialize func_dir
func_dir = ida_dirtree.get_std_dirtree(ida_dirtree.DIRTREE_FUNCS)
ite = ida_dirtree.dirtree_iterator_t()
ok = func_dir.findfirst(ite, "*")

def get_func_dir():
    """
    Get the func_dir object for folder operations.
    """
    return func_dir
