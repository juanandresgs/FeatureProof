"""
    FeatureProof Middleware function: get_qword_at_address.py

    Get QWORD at address.

    :param address: Address to get QWORD from.
    :return: QWORD at address as an integer.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.get_qword(address)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get QWORD at address',
            'parameters': 'address',
            'return_type': 'int'
        },
    }
