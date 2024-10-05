"""
    FeatureProof Middleware function: rename_function.py

    Rename a function at a given address.

    :param ea: Address of the function.
    :param new_name: New name for the function.
    :return: Boolean indicating success.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6(ea, new_name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea, new_name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.set_name(ea, new_name, idc.SN_NOWARN)

def function_9(ea, new_name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Rename a function at a given address.',
            'parameters': ['ea', 'new_name'],
            'return_type': 'bool'
        },
    }
