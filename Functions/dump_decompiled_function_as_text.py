"""
    FeatureProof Middleware function: dump_decompiled_function_as_text.py

    Dumps the decompiled pseudocode of the function at the given address.

    :param ea: The address of the function to decompile.
    :return: None
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    f = ida_funcs.get_func(ea)
    if not f:
        logger.warning(f"Function not found at 0x{ea:x}")
        return

    cfunc = ida_hexrays.decompile(ea)
    if not cfunc:
        logger.warning(f"Failed to decompile function at 0x{ea:x}")
        return

    pseudocode = cfunc.get_pseudocode()
    for line in pseudocode:
        print(ida_lines.tag_remove(line.line))

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Dumps the decompiled pseudocode of the function at the given address.',
            'parameters': ['ea'],
            'return_type': 'None'
        },
    }
