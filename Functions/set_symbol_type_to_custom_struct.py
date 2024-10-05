"""
    FeatureProof Middleware function: set_symbol_type_to_custom_struct.py

    Set the type of a symbol at the given address to a custom struct.

    :param ea: The address of the symbol.
    :param struct_name: The name of the custom struct.
    :return: True if the type was set successfully, False otherwise.
"""
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]

def function_6(ea, struct_name):
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(ea, struct_name):
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    try:
        # Get the structure ID
        sid = ida_struct.get_struc_id(struct_name)
        if sid == idaapi.BADADDR:
            print(f"Structure '{struct_name}' not found.")
            return False

        # Get the size of the structure
        struct_size = ida_struct.get_struc_size(sid)
        if struct_size == 0:
            print(f"Structure '{struct_name}' has size 0.")
            return False

        if not ida_bytes.create_struct(ea, struct_size, sid):
            print(f"Failed to create structure '{struct_name}' at address {hex(ea)}.")
            return False

        print(f"Successfully set the type of the symbol at address {hex(ea)} to '{struct_name}'.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def function_9(ea, struct_name):
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Set the type of a symbol at the given address to a custom struct.',
            'parameters': ['ea', 'struct_name'],
            'return_type': 'bool'
        },
    }
