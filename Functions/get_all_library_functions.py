"""
    FeatureProof Middleware function: get_all_library_functions.py

    Get all library functions in the binary.

    :return: List of function addresses.
"""
from FunctionInfo import TYPE_FUNC_LIB
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8():
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return get_all_functions_by_type_return_addresses(TYPE_FUNC_LIB)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get all library functions in the binary.',
            'parameters': [],
            'return_type': 'List[int]'
        },
    }
