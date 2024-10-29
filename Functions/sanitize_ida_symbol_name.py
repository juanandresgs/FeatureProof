"""
    FeatureProof Middleware function: sanitize_ida_symbol_name.py

    Replaces characters in a string that can't be used in IDA Pro symbol names with an underscore.

    :param name: The string to be sanitized.
    :return: A sanitized string that can be used as an IDA Pro symbol name.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    pattern = re.compile(r'[^a-zA-Z0-9_]')
    sanitized_name = pattern.sub('_', name)
    if sanitized_name and sanitized_name[0].isdigit():
        sanitized_name = '_' + sanitized_name
    return sanitized_name

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Replaces characters in a string that can\'t be used in IDA Pro symbol names with an underscore.',
            'parameters': ['name'],
            'return_type': 'str'
        },
    }
