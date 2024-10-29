"""
    FeatureProof Middleware: TypeInfo.py

    Abstracted basic type info to standardardize use across middleware functions.
"""

"""
    #TODO: Missing a logic to parse out types for IDA Pro vs Binary Ninja vs Ghidra, hence abstraction.
"""

# Operand Types
TYPE_VOID = idc.o_void        0  // No Operand                           ----------
TYPE_REGISTER = idc.o_reg         1  // General Register (al, ax, es, ds...) reg
TYPE_MEM = idc.o_mem         2  // Direct Memory Reference  (DATA)      addr
TYPE_PHRASE = idc.o_phrase      3  // Memory Ref [Base Reg + Index Reg]    phrase
TYPE_DISPLACEMENT = idc.o_displ       4  // Memory Reg [Base Reg + Index Reg + Displacement] phrase+addr
TYPE_IMMEDIATE = idc.o_imm         5  // Immediate Value                      value
TYPE_FARADDR = idc.o_far         6  // Immediate Far Address  (CODE)        addr
TYPE_NEARADDR = idc.o_near        7  // Immediate Near Address (CODE)        addr

// x86
TYPE_TRREG = idc.o_trreg         o_idpspec0      // trace register
TYPE_DBREG = idc.o_dbreg         o_idpspec1      // debug register
TYPE_CRREG = idc.o_crreg         o_idpspec2      // control register
TYPE_FPREG = idc.o_fpreg         o_idpspec3      // floating point register
TYPE_MMXREG = idc.o_mmxreg        o_idpspec4      // mmx register
TYPE_XMMREG = idc.o_xmmreg        o_idpspec5      // xmm register

// arm
TYPE_REGLIST = idc.o_reglist       o_idpspec1      // Register list (for LDM/STM)
TYPE_CREGLIST = idc.o_creglist      o_idpspec2      // Coprocessor register list (for CDP)
TYPE_CREG = idc.o_creg          o_idpspec3      // Coprocessor register (for LDC/STC)
TYPE_FPREGLIST = idc.o_fpreglist     o_idpspec4      // Floating point register list
TYPE_TEXT = idc.o_text          o_idpspec5      // Arbitrary text stored in the operand
TYPE_COND = idc.o_cond          (o_idpspec5+1)  // ARM condition as an operand

# Address Types
BADADDR = idc.BADADDR // Does this concept exist in Binja/Ghidra?

# Data Types
TYPE_QWORD = idaapi.FF_QWORD
TYPE_DWORD = idaapi.FF_DWORD
