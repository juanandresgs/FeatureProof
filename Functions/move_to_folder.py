"""
    FeatureProof Middleware function: move_to_folder.py

    Move a function by name to a specified folder in IDA Pro.

    :param func_name: Name of the function to move.
    :param folder_name: Name of the target folder.
    :return: Boolean indicating success.
"""
from FeatureProof.FolderInfo import get_func_dir
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(func_name, folder_name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(func_name, folder_name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    if not fp.check_folder_exists(folder_name):
        logger.error(f"Folder named: {folder_name} does not exist!")
        fp.create_folder(folder_name)
    func_dir = get_func_dir()
    return func_dir.rename(func_name, folder_name + "/" + func_name)

def function_9(func_name, folder_name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Move a function to a specified folder in IDA Pro.',
            'parameters': ['func_name', 'folder_name'],
            'return_type': 'bool'
        },
    }
