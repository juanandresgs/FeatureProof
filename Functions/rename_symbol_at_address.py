"""
    FeatureProof Middleware function: rename_symbol_at_address.py

    Renames the symbol at the given address.

    :param address: The address of the symbol to rename.
    :param new_name: The new name for the symbol.
    :return: None
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(address, new_name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    if idc.set_name(address, new_name, idc.SN_CHECK):
        logger.info(f"Symbol at 0x{address:X} renamed to {new_name}.")
    else:
        logger.warning(f"Failed to rename symbol at 0x{address:X}.")
        (f"Failed to rename symbol at 0x{address:X}.")

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Renames the symbol at the given address.',
            'parameters': ['address', 'new_name'],
            'return_type': 'None'
        },
    }
