"""
    FeatureProof Middleware function: get_all_xref_addresses_to_this_address.py

    Get all cross-reference addresses to a given address.

    :param ea: The address to find cross-references to.
    :return: List of cross-reference addresses.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    fp.check_type_is(ea)
    try:
        return [fp.format_address(ref.frm) for ref in idautils.XrefsTo(ea)]
    except Exception as e:
        logger.error(f"Error: {e}")
        return []

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get all cross-reference addresses to a given address.',
            'parameters': ['ea'],
            'return_type': 'List[int]'
        },
    }
