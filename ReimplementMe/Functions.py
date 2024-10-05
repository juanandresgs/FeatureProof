#    Works
def get_all_library_functions():
    return get_all_functions_by_type_return_addresses(TYPE_FUNC_LIB)

#    Works
def get_all_lumina_functions():
    return get_all_functions_by_type_return_addresses(TYPE_FUNC_LUMINA)

#    Works
def get_all_thunk_functions():
    return get_all_functions_by_type_return_addresses(TYPE_FUNC_THUNK)

#    Works
def rename_function(ea, new_name):
    return idc.set_name(ea, new_name, idc.SN_NOWARN)

#    Works
def get_function_name_from_address(ea):
    return idc.get_func_name(ea)

#    Works
def reset_function_name(ea):
    return rename_function(ea, "")

#    Works
def get_function_address_from_name(name):
    return format_address(idc.get_name_ea_simple(name))

#   Works
def get_function_boundaries(ea):
    func = ida_funcs.get_func(ea)
    return format_address(func.start_ea), format_address(func.end_ea-1)

#   Works
class FunctionInfo:
    def print_info(self):
        print(f"Start EA: {format_address(self.start_ea)}")
        print(f"End EA: {format_address(self.end_ea)}")
        print(f"Size: {'0x{:X}'.format(self.size)}")
        print(f"Flags: {'0x{:X}'.format(self.flags)}")
        print(f"Returns?: {self.does_return}")

    def __init__(self, start_ea, end_ea, size, flags, does_return):
        self.start_ea = start_ea
        self.end_ea = end_ea
        self.size = size
        self.flags = flags
        self.does_return = does_return
