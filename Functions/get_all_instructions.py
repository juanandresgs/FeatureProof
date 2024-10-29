"""
    FeatureProof Middleware function: get_all_instructions.py

    Get all instructions (in range).

    :param start_ea: Start address (Optional).
    :param end_ea: End address (Optional).
    :return: All instructions in range.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(start_ea=None, end_ea=None):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idautils.Heads(start_ea, end_ea)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get all instructions',
            'parameters': ['start_ea', 'end_ea'],
            'return_type': 'generator'
        },
    }
