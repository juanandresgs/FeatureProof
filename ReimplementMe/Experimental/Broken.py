
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
    xrefs = [format_address(ref.frm) for ref in idautils.XrefsTo(func.start_ea)]
    for head in idautils.Heads(func.start_ea, func.end_ea):
        xrefs.extend([format_address(ref.frm) for ref in idautils.XrefsTo(head)])
    return xrefs
