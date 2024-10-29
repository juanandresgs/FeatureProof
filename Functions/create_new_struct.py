"""
    FeatureProof Middleware function: create_new_struct.py

    Create a new structure by name.

    :param name: Name of the structure to create.
    :return: The sid of the structure if it exists, False otherwise.
"""
from FeatureProof.TypeInfo import BADADDR
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_8(name):
    sid = fp.check_if_struct_exists(name)
    if sid is not False:
        logger.debug(f"Structure {name} already exists.")
        return sid

    sid = idc.add_struc(-1, name, 0)
    if sid == BADADDR:
        print(f"Failed to create structure {name}.")
        return False
    return sid

def get_function():
    """
        Only return available implementations.
    """
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Create a struct by name and get the sid',
            'parameters': ['name'],
            'return_type': 'sid or False'
        },
    }
