"""
    FeatureProof Middleware function: get_function_name_from_address.py

    Get the name of the function at a given address.

    :param ea: The address of the function.
    :return: The name of the function.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.get_func_name(ea)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get the name of the function at a given address.',
            'parameters': ['ea'],
            'return_type': 'str'
        },
    }
