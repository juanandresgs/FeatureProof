"""
    FeatureProof Middleware function: reset_function_name.py

    Reset the name of a function at a given address.

    :param ea: Address of the function.
    :return: Boolean indicating success.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6(ea):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return fp.rename_function(ea, "")

def function_9(ea):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Reset the name of a function at a given address.',
            'parameters': ['ea'],
            'return_type': 'bool'
        },
    }
