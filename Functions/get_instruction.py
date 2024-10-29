"""
    FeatureProof Middleware function: get_instruction.py

    Get instruction mnemonic at address

    :param instruction_address: Address of the instruction.
    :return: Instruction mnemonic as a string.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(instruction_address):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    return idc.print_insn_mnem(instruction_address)

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get instruction mnemonic at address.',
            'parameters': 'instruction_address',
            'return_type': 'string'
        },
    }
