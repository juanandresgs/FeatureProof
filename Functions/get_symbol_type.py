"""
    FeatureProof Middleware function: get_symbol_type.py

    Get the type of a symbol at a given address.

    :param symbol_address: Address of the symbol or name of symbol
    :return: str type of the symbol
"""
import os
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(): # Add parameters as needed
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")
    # Implementation for IDA Pro 6.8-7.x

def function_8(symbol_address): # Add parameters as needed
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    # if argument is a string, convert it to an address
    if isinstance(symbol_address, str):
        symbol_address = fp.get_function_address_from_name(symbol_address)
    return idc.get_type(symbol_address)

def function_9(): # Add parameters as needed
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")
    # Implementation for IDA Pro 9+

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get the type of a symbol at a given address.',
            'parameters': 'symbol_address',
            'return_type': 'str'
        },
    }
