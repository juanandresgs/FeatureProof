"""
    FeatureProof Middleware function: walk_functions_return_names.py

    Walk through all functions in the binary and return their names.

    :return: List of function names.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8():
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return [fp.get_function_name_from_address(func) for func in fp.walk_functions()]

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Walk through all functions in the binary and return their names.',
            'parameters': [],
            'return_type': 'List[str]'
        },
    }
