"""
    FeatureProof Middleware function: check_if_struct_exists.py

    Check if a structure exists by name and get the sid.

    :param name: Name of the structure to check.
    :return: The sid of the structure if it exists, False otherwise.
"""
from FeatureProof.TypeInfo import BADADDR
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_8(name):
    sid = idc.get_struc_id(name)
    if sid == BADADDR:
        logger.debug(f"Structure {name} not exist.")
        return False
    logger.debug(f"Structure {name} exists.")
    return sid

def get_function():
    """
        Only return available implementations.
    """
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Check if a structure exists by name and get the sid',
            'parameters': ['name'],
            'return_type': 'sid or False'
        },
    }
