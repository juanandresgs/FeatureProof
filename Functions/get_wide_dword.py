"""
    FeatureProof Middleware function: get_operand_type.py

    Get instruction operand type by index.

    :param instruction_address: Address of the instruction.
    :param operand_index: Index of the operand.
    :return: Operand type
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(current_address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.get_wide_dword(current_address)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get operand type',
            'parameters': ['instruction_address', 'operand_index'],
            'return_type': 'int'
        },
    }