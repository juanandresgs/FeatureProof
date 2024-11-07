"""
    FeatureProof Middleware function: get_all_function_addresses_by_type.py

    Get all functions of a specific type and return their addresses.

    :param func_type: The type of functions to retrieve.
    :return: List of function addresses.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
from FeatureProof.FunctionInfo import *
logger = fp.logger


def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(func_type):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    functions = []
    for func_ea in fp.walk_functions():
        logger.debug(f"Function: {fp.format_address(func_ea)}")
        if idaapi.get_func(func_ea).flags & func_type: #TODO: Should this be abstracted independently?
            logger.debug(f"  Function of type {func_type} found: {fp.format_address(func_ea)}")
            functions.append(fp.format_address(func_ea))
    logger.debug(f"Found {len(functions)} functions of type {func_type}")
    return functions

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get all functions of a specific type and return their addresses.',
            'parameters': ['func_type'],
            'return_type': 'List[int]'
        },
    }
