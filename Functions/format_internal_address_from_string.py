"""
    FeatureProof Middleware function: format_internal_address_from_string.py

    Convert an address in hexadecimal string format to an integer.

    :param addr_str: The address in hexadecimal string format.
    :return: The address as an integer.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(addr_str):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return int(addr_str, 16)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Convert an address in hexadecimal string format to an integer.',
            'parameters': ['addr_str'],
            'return_type': 'int'
        },
    }
