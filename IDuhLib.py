# idapython_lib.py
import idaapi
import idc
import idautils
import ida_struct
import ida_funcs
import ida_segment
import ida_xref
import ida_bytes
import ida_typeinf
import ida_dirtree


##################################
######UNIVERSAL UTILITIES#########
##################################
# Utility function to format addresses in hexadecimal
#    Works
def format_address(ea): # Works
    return "0x{:08X}".format(ea)

#    Works
def format_internal_address_from_hex(ea):
    return ea

#    Works
def format_internal_address_from_string(addr_str):
    return int(addr_str, 16)

##################################
###########FUNCTIONS##############
##################################
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

def get_function_info_object(ea) -> FunctionInfo:
    func = ida_funcs.get_func(ea)
    if func is None:
        return None
    # Extracting relevant attributes
    start_ea = func.start_ea
    end_ea = func.end_ea-1
    size = func.size()
    flags = func.flags
    does_return = func.does_return()
    return FunctionInfo(start_ea, end_ea, size, flags, does_return)

def print_function_info_summary(ea):
    get_function_info_object(ea).print_info()

##################################
######STRUCTURES AND TYPES########
##################################

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

#   Untested
def change_symbol_type(ea, new_type):
    til = idaapi.get_idati()
    tinfo = idaapi.tinfo_t()
    if ida_typeinf.parse_decl(tinfo, til, new_type, ida_typeinf.PT_SIL):
        return idaapi.apply_tinfo(ea, tinfo, idaapi.TINFO_DEFINITE)
    return False

#   Untested
def change_function_prototype(ea, prototype):
    return change_symbol_type(ea, prototype)

#   Untested
def read_function_prototype(ea):
    tinfo = idaapi.tinfo_t()
    if idaapi.get_tinfo(tinfo, ea):
        return str(tinfo)
    return ""

#   Untested
def apply_struct_type(ea, struct_name):
    struct_id = ida_struct.get_struc_id(struct_name)
    struct_size = ida_struct.get_struc_size(struct_id)
    return ida_bytes.del_items(ea, ida_bytes.DELIT_SIMPLE, struct_size) == struct_size and \
           ida_bytes.create_struct(ea, struct_size, struct_id)

##################################
###########FOLDER OPS#############
##################################

func_dir: ida_dirtree.dirtree_t
func_dir =   ida_dirtree.get_std_dirtree(ida_dirtree.DIRTREE_FUNCS)
ite = ida_dirtree.dirtree_iterator_t()
ok = func_dir.findfirst(ite, "*")

#works
def create_folder(name):
    """
    Create a folder in IDA Pro.
    """
    return func_dir.mkdir(name)

#works if folder is empty
def delete_folder(name):
    """
    Delete a folder in IDA Pro.

    Works only if the folder is empty! 
    """
    # Missing call to "empty_folder()"
    return func_dir.rmdir(name)

"""
def empty_folder(folder_name):
    Not sure how to do this yet
"""


#works
def move_to_folder(func_name, folder_name):
    """
    Move a function to a specified folder in IDA Pro.
    """
    return func_dir.rename(func_name, folder_name+"/"+func_name)

#works
def check_folder_exists(folder_name):
    """
    Check if a folder exists in IDA Pro.
    """
    return func_dir.isdir(folder_name)


##################################
############SEGMENTS############## 
##################################
def walk_segment(segment_start):
    return [format_address(ea) for ea in idautils.Heads(segment_start, idc.get_segm_end(segment_start))]

def edit_segment_name_and_boundaries(segment_start, new_name, new_start, new_end):
    seg = ida_segment.getseg(segment_start)
    if seg:
        ida_segment.set_segm_name(seg, new_name)
        ida_segment.set_segm_start(seg, new_start, ida_segment.SEGMOD_KEEP)
        ida_segment.set_segm_end(seg, new_end, ida_segment.SEGMOD_KEEP)

def create_segment(start, end, name, segment_class):
    segm = ida_segment.segment_t()
    segm.start_ea = start
    segm.end_ea = end
    segm.sel = idaapi.setup_selector(0)
    segm.type = idaapi.SEG_CODE
    ida_segment.add_segm_ex(segm, name, segment_class, ida_segment.ADDSEG_OR_DIE)

##################################
############XREFs#################
##################################

#   Works
def get_all_xref_addresses_to_this_address(ea):
    return [format_address(ref.frm) for ref in idautils.XrefsTo(ea)]

"""
def get_all_xref_addresses_to_this_name(symbol_name):
    resolved = <xxx(symbol_name)>resolve name at address?
    get_all_xref_addresses_to_this_address(resolved)
"""

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

######################
# IDEAS TO IMPLEMENT #
######################
"""
    Get all symbols referred to within a function
"""
"""
    Get all references to a given symbol name
"""
"""
    Get function at address
"""
"""
    Get segment name at address
"""
"""
    Get value of first operand
"""
"""
    Get value of second operand
"""
"""
    Get function argument values at XREFs
"""
"""
    Get symbol type
"""
"""
    Make comment at address
"""
"""
    Get XREFs to symbol
"""
"""
    Get XREFs to address
"""
"""
    Get XREFs from address
"""
"""
    Get descending call graph from starting function
"""
"""
    Get ascending call graph from starting function
"""
"""
    Get XREF count to symbol  
"""
"""
    def list_all_segments():
"""
"""
    def list_all_segments_by_name():
"""
"""
    def list_all_segments_by_starting_address():
"""
"""
    def determine_start_of_segment_at_address(ea):
"""
"""
    List functions in a specified folder in IDA Pro.
    def list_functions_in_folder(folder_name):
"""
"""
    def move_folder(src_folder_name, dest_folder_name):
    Move all functions from one folder to another in IDA Pro.
"""
"""
    def empty_folder(folder_name):
"""
