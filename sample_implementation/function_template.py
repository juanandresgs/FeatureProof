"""
    FeatureProof Middleware function: function_template.py

    <description>

    :param: <...>
    :return: <...>
"""
"""
    Make sure imports are added to the import injection function under the relevant version. Do not import from within the function implementation file.
"""

filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
def function_6():
    """
        Example function for IDA Pro 6.8-7.x
    """
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8():
    """
        Example function for IDA Pro 7.x-8.4
    """
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")

def function_9():
    """
        Example function for IDA Pro 9+
    """
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    """
        Only return available implementations.
    """
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        6: {
            'implementation': function_6,
            'description': 'Example function for IDA Pro 6.8-7.x',
            'parameters': [],
            'return_type': 'None'
        },
        8: {
            'implementation': function_8,
            'description': 'Example function for IDA Pro 7.x-8.4',
            'parameters': [],
            'return_type': 'None'
        },
        9: {
            'implementation': function_9,
            'description': 'Example function for IDA Pro 9+',
            'parameters': [],
            'return_type': 'None'
        },
    }
