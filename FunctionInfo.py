"""
    FeatureProof Middleware: FunctionInfo.py

    Define function type enums and FunctionInfo class for use in other middleware functions.
"""

# Function type enums
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

# FunctionInfo class
class FunctionInfo:
    def print_info(self):
        print(f"Start EA: {fp.format_address(self.start_ea)}")
        print(f"End EA: {fp.format_address(self.end_ea)}")
        print(f"Size: {'0x{:X}'.format(self.size)}")
        print(f"Flags: {'0x{:X}'.format(self.flags)}")
        print(f"Returns?: {self.does_return}")

    def __init__(self, start_ea, end_ea, size, flags, does_return):
        self.start_ea = start_ea
        self.end_ea = end_ea
        self.size = size
        self.flags = flags
        self.does_return = does_return
