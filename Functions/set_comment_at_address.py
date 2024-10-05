"""
    FeatureProof Middleware function: set_comment_at_address.py

    Set a comment at a given address in IDA Pro.

    :param ea: The address where the comment should be set.
    :param comment: The comment text to set.
    :param is_repeatable: Boolean indicating if the comment should be repeatable. Default is False.
    :return: True if the comment was set successfully, False otherwise.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea, comment, is_repeatable=False):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    try:
        # Set the comment at the given address
        result = idc.set_cmt(ea, comment, is_repeatable)

        if result:
            logger.info(f"Successfully set the comment at address {hex(ea)}.")
            return True
        else:
            logger.warning(f"Failed to set the comment at address {hex(ea)}.")
            return False
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return False

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Set a comment at a given address in IDA Pro.',
            'parameters': ['ea', 'comment', 'is_repeatable'],
            'return_type': 'bool'
        },
    }
