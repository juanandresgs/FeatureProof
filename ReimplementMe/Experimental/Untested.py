def get_strings_intersection_of_start_and_end(start_substr, end_substr, min_length=4):
    """
    Retrieve the union of strings that start with or end with a specific substring and with a minimum length.

    :param substr: The substring to filter strings.
    :param min_length: Minimum length of strings to be retrieved.
    :return: Set of tuples containing (address, string).
    """
    starting_strings = set(fp.get_strings_starting_with(start_substr, min_length))
    ending_strings = set(fp.get_strings_ending_with(end_substr, min_length))
    return starting_strings.intersection(ending_strings)

##################################
############SEGMENTS##############
##################################
def walk_segment(segment_start):
    return [fp.format_address(ea) for ea in idautils.Heads(segment_start, idc.get_segm_end(segment_start))]

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

def get_segment_name_at_address(ea):
    """
    Get the segment name at a given address.

    :param ea: Address to check the segment name
    :return: Name of the segment or None if not found
    """
    # Ensure ea is of type ea_t
    check_type_is(ea, int)

    segment = ida_segment.getseg(ea)
    if segment:
        segment_name = ida_segment.get_segm_name(segment)
        return segment_name
    else:
        return None

########
#   Untested
def change_function_prototype(ea, prototype):
    return fp.change_symbol_type(ea, prototype)

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
    fp.get_function_info_object(ea).print_info()
