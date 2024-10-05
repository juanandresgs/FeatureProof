#    Works
def walk_functions():
    return idautils.Functions()

#    Works
def walk_functions_return_addresses():
    return [format_address(func) for func in walk_functions()]

#    Works
def walk_functions_return_names():
    return [get_function_name_from_address(func) for func in walk_functions()]

TYPE_FUNC_NORET = 0x00000001
TYPE_FUNC_FAR = 0x00000002
TYPE_FUNC_LIB = 0x00000004
TYPE_FUNC_STATIC = 0x00000008
TYPE_FUNC_FRAME = 0x00000010
TYPE_FUNC_USERFAR = 0x00000020
TYPE_FUNC_HIDDEN = 0x00000040
TYPE_FUNC_THUNK = 0x00000080
TYPE_FUNC_BOTTOMBP = 0x00000100
TYPE_FUNC_NORET_PENDING = 0x00000200
TYPE_FUNC_SP_READY = 0x00000400
TYPE_FUNC_FUZZY_SP = 0x00000800
TYPE_FUNC_PROLOG_OK = 0x00001000
TYPE_FUNC_PURGED_OK = 0x00004000
TYPE_FUNC_TAIL = 0x00008000
TYPE_FUNC_LUMINA = 0x00010000
TYPE_FUNC_OUTLINE = 0x00020000

#    Works
def get_all_functions_by_type_return_addresses(func_type):
    functions = []
    for func_ea in walk_functions():
        if idaapi.get_func(func_ea).flags & func_type:
            functions.append(format_address(func_ea))
    return functions

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
