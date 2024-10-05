"""
    FeatureProof Middleware function: get_function_boundaries.py

    Get the start and end addresses of a function.

    :param ea: Address of the function.
    :return: Tuple of start and end addresses.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6(ea):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    func = ida_funcs.get_func(ea)
    return fp.format_address(func.start_ea), fp.format_address(func.end_ea-1)

def function_9(ea):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get the start and end addresses of a function.',
            'parameters': ['ea'],
            'return_type': 'Tuple[int, int]'
        },
    }
