"""
    FeatureProof Middleware function: format_address.py

    Format an address as a hex string.

    :param ea: Address to be formatted.
    :return: Formatted address as a string.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return "0x{:08X}".format(ea)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        # 6: {
        #     'implementation': function_6,
        #     'description': 'Example function for IDA Pro 6.8-7.x',
        #     'parameters': [],
        #     'return_type': 'None'
        # },
        8: {
            'implementation': function_8,
            'description': 'format_address',
            'parameters': ['ea'],
            'return_type': 'str'
        },
        # 9: {
        #     'implementation': function_9,
        #     'description': 'Example function for IDA Pro 9+',
        #     'parameters': [],
        #     'return_type': 'None'
        # },
    }
