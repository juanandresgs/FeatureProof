"""
    FeatureProof Middleware function: check_type_is.py

    Check if a variable is of a specified type.

    :param var: The variable to check.
    :param wanted: The type to check against.
    :return: None
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(var, wanted=int):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    if not isinstance(var, wanted):
        raise TypeError(f"Expected variable to be of type {wanted}, got {type(var)} instead.")

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Check if a variable is of a specified type.',
            'parameters': ['var', 'wanted'],
            'return_type': 'None'
        },
    }
