"""
    FeatureProof Middleware function: get_strings_containing_substr.py

    Retrieve all strings in the binary containing a specific substring and with a minimum length.

    :param substr: The substring to filter strings.
    :return: List of tuples containing (address, string).
    Retrieve all strings in the binary with a minimum length.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(substr, min_length=4):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return [s for s in fp.get_all_strings(min_length) if substr in s[1]]

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'get_strings_containing_substr',
            'parameters': [],
            'return_type': 'None'
        },
    }
