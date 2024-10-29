"""
    FeatureProof Middleware function: get_previous_instruction_address.py

    Get previous instruction address.

    :param : Current instruction address.
    :return: Previous instruction address.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(current_instruction_address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.prev_head(current_instruction_address)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get previous instruction address',
            'parameters': 'current_instruction_address',
            'return_type': 'address'
        },
    }
