func_dir: ida_dirtree.dirtree_t
func_dir = ida_dirtree.get_std_dirtree(ida_dirtree.DIRTREE_FUNCS)
ite = ida_dirtree.dirtree_iterator_t()
ok = func_dir.findfirst(ite, "*")

#works
def create_folder(name):
    """
    Create a folder in IDA Pro.
    """
    return func_dir.mkdir(name)

#works if folder is empty
def delete_folder(name):
    """
    Delete a folder in IDA Pro.

    Works only if the folder is empty!
    """
    # Missing call to "empty_folder()"
    return func_dir.rmdir(name)

"""
def empty_folder(folder_name):
    Not sure how to do this yet
"""

#works
def move_to_folder(func_name, folder_name):
    """
    Move a function to a specified folder in IDA Pro.
    """
    return func_dir.rename(func_name, folder_name+"/"+func_name)

#works
def check_folder_exists(folder_name):
    """
    Check if a folder exists in IDA Pro.
    """
    return func_dir.isdir(folder_name)
