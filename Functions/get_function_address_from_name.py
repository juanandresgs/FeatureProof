"""
    FeatureProof Middleware function: get_function_address_from_name.py

    Get the address of a function by its name.

    :param name: Name of the function.
    :return: Address of the function.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6(name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return format_address(idc.get_name_ea_simple(name))

def function_9(name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get the address of a function by its name.',
            'parameters': ['name'],
            'return_type': 'int'
        },
    }
