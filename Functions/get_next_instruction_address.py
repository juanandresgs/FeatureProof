"""
    FeatureProof Middleware function: get_next_instruction_address.py

    Check if a folder exists in IDA Pro.

    :param folder_name: Name of the folder to check.
    :return: Boolean indicating existence.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(instruction_address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.next_head(instruction_address)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get next instruction address',
            'parameters': 'instruction_address',
            'return_type': 'address'
        },
    }
