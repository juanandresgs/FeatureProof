"""
    FeatureProof Middleware function: get_all_lumina_functions.py

    Get all Lumina functions in the binary.

    :return: List of function addresses.
"""
from FeatureProof.FunctionInfo import TYPE_FUNC_LUMINA
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8():
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return fp.get_all_function_addresses_by_type(TYPE_FUNC_LUMINA)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get all Lumina functions in the binary.',
            'parameters': [],
            'return_type': 'List[int]'
        },
    }
