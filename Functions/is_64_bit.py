"""
    FeatureProof Middleware function: is_64bit.py

    Determine if the analyzed sample is 64-bit.

    :return: True if the sample is 64-bit, False if it is 32-bit.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8():
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idaapi.inf_is_64bit()

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Determine if the analyzed sample is 64-bit.',
            'parameters': [],
            'return_type': 'bool'
        },
    }
