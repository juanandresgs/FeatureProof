"""
    FeatureProof Middleware function: delete_folder.py

    Delete a folder in IDA Pro.

    Works only if the folder is empty!

    :param name: Name of the folder to delete.
    :return: Boolean indicating success.
"""
from FeatureProof.FolderInfo import get_func_dir
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    func_dir = get_func_dir()
    #TODO: Check folder exists, check if folder is empty?
    return func_dir.rmdir(name)

def function_9(name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Delete a folder in IDA Pro. Works only if the folder is empty!',
            'parameters': ['name'],
            'return_type': 'bool'
        },
    }
