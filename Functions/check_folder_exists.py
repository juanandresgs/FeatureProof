"""
    FeatureProof Middleware function: check_folder_exists.py

    Check if a folder exists in IDA Pro.

    :param folder_name: Name of the folder to check.
    :return: Boolean indicating existence.
"""
from FeatureProof.FolderInfo import get_func_dir
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(folder_name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(folder_name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    func_dir = get_func_dir()
    return func_dir.isdir(folder_name)

def function_9(folder_name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Check if a folder exists in IDA Pro.',
            'parameters': ['folder_name'],
            'return_type': 'bool'
        },
    }
