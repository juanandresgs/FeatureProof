"""
    FeatureProof Middleware function: get_wide_word.py

    Get a wide word (2 bytes) value from the specified address.

    :param address: The address to read the wide word from.
    :return: The wide word value at the specified address.
"""
import os
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(address):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")
    # Implementation for IDA Pro 6.8-7.x

def function_8(address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return ida_bytes.get_wide_word(address)

def function_9(address):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")
    # Implementation for IDA Pro 9+

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get a wide word (2 bytes) value from the specified address.',
            'parameters': ['address'],
            'return_type': 'int'
        },
    } 