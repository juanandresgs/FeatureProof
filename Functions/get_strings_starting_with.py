"""
    FeatureProof Middleware function: get_strings_starting_with.py

    Retrieve all strings in the binary that start with a specific substring and with a minimum length.

    :param substr: The substring to filter strings.
    :param min_length: Minimum length of strings to be retrieved.
    :return: List of tuples containing (address, string).
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(substr, min_length=4):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return [s for s in fp.get_all_strings(min_length) if s[1].startswith(substr)]

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Retrieve all strings in the binary that start with a specific substring and with a minimum length.',
            'parameters': ['substr', 'min_length'],
            'return_type': 'List[Tuple[int, str]]'
        },
    }
