"""
    FeatureProof Middleware function: walk_functions.py

    Walk through all functions in the binary.

    :return: Iterator of function addresses.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8():
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idautils.Functions()

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Walk through all functions in the binary.',
            'parameters': [],
            'return_type': 'Iterator[int]'
        },
    }
