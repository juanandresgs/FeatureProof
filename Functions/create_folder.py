"""
    FeatureProof Middleware function: create_folder.py

    Create a folder in IDA Pro.

    :param name: Name of the folder to create.
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
    return func_dir.mkdir(name)

def function_9(name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Create a folder in IDA Pro.',
            'parameters': ['name'],
            'return_type': 'bool'
        },
    }
