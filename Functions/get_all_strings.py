"""
    FeatureProof Middleware function: get_all_strings.py

    Retrieve all strings in the binary with a minimum length.

    :param min_length: Minimum length of strings to be retrieved.
    :return: List of tuples containing (address, string).
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(min_length=4):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    strings = []
    for s in idautils.Strings():
        if len(str(s)) >= min_length:
            strings.append((fp.format_address(s.ea), str(s)))
    return strings

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
            'description': 'get_all_strings',
            'parameters': [],
            'return_type': 'None'
        },
        # 9: {
        #     'implementation': function_9,
        #     'description': 'Example function for IDA Pro 9+',
        #     'parameters': [],
        #     'return_type': 'None'
        # },
    }
