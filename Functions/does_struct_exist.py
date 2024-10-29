"""
    FeatureProof Middleware function: does_struct_exist.py

    Check if a struct with a specific name exists in the IDA database.

    :param struct_name: Name of the struct to check.
    :return: True if the struct exists, False otherwise.
"""
from FeatureProof.TypeInfo import BADADDR
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(struct_name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(struct_name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    sid = ida_struct.get_struc_id(struct_name)
    return sid != BADADDR

def function_9(struct_name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Check if a struct with a specific name exists in the IDA database.',
            'parameters': ['struct_name'],
            'return_type': 'bool'
        },
    }
