"""
    FeatureProof Middleware function: get_segment_name_at_address.py

    Get the segment name at a given address.

    :param instruction_address: Address to check the segment name
    :return: Name of the segment or None if not found
"""
import os
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")
    # Implementation for IDA Pro 6.8-7.x

def function_8(instruction_address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    # Ensure instruction_address is of type ea_t
    fp.check_type_is(instruction_address, int)

    segment = ida_segment.getseg(instruction_address)
    if segment:
        segment_name = ida_segment.get_segm_name(segment)
        return segment_name
    else:
        return None

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")
    # Implementation for IDA Pro 9+

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get the segment name at a given address.',
            'parameters': 'instruction_address',
            'return_type': 'str or None'
        },
    }
