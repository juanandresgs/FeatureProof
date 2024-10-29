
#   DOESNT WORK, unrelated addresses outputted
def get_all_xrefs_from_within_function(ea):
    xrefs = []
    func = ida_funcs.get_func(ea)
    for head in idautils.Heads(func.start_ea, func.end_ea):
        xrefs.extend([format_address(ref.to) for ref in idautils.XrefsFrom(head)])
    return xrefs

#   DOESNT WORK, unrelated addresses outputted
def get_all_xrefs_to_function(ea):
    func = ida_funcs.get_func(ea)
    xrefs = [fp.format_address(ref.frm) for ref in idautils.XrefsTo(func.start_ea)]
    for head in idautils.Heads(func.start_ea, func.end_ea):
        xrefs.extend([fp.format_address(ref.frm) for ref in idautils.XrefsTo(head)])
    return xrefs

# "guess_type_size" doesn't work'
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
