# Works
def does_struct_exist(struct_name):
    """
    Check if a struct with a specific name exists in the IDA database.

    :param struct_name: Name of the struct to check.
    :return: True if the struct exists, False otherwise.
    """
    sid = ida_struct.get_struc_id(struct_name)
    return sid != ida_idaapi.BADADDR

#   Untested
def create_struct_type(struct_name, size, fields):
    """
    Creates a structure and adds fields to it.

    :param struct_name: Name of the structure
    :param size: Size of the structure
    :param fields: List of tuples with field definitions (name, offset, type)
    :return: Structure ID or BADADDR if creation failed
    """
    sid = idaapi.add_struc(idaapi.BADADDR, struct_name, False)
    if sid != idaapi.BADADDR:
        struct = ida_struct.get_struc(sid)
        if struct:
            struct.size = size  # Set structure size directly

            for field_name, field_offset, field_type in fields:
                flag, typeid = idc.guess_type_size(field_type)

                if flag is None:
                    print(f"Invalid type {field_type} for field {field_name}")
                    return idaapi.BADADDR

                ida_struct.add_struc_member(
                    struct,
                    field_name,
                    field_offset,
                    flag,
                    None,
                    typeid
                )
        else:
            return idaapi.BADADDR

    return sid

# Works
def set_symbol_type_to_custom_struct(ea, struct_name):
    """
    Set the type of a symbol at the given address to a custom struct.

    :param ea: The address of the symbol.
    :param struct_name: The name of the custom struct.
    :return: True if the type was set successfully, False otherwise.
    """
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

        # # Optionally, rename the symbol at the address
        # idc.set_name(ea, struct_name, idc.SN_CHECK)

        print(f"Successfully set the type of the symbol at address {hex(ea)} to '{struct_name}'.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
