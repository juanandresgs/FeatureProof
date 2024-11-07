import idaapi
idaapi.require("FeatureProof.FeatureProof")
from FeatureProof.FeatureProof import Middleware

fp = Middleware()
fp.set_logging_level(level=logging.INFO)
logger = fp.logger

try:
    # print(fp.get_all_strings())
    # print(fp.get_strings_containing_substr("cargo"))
    # print(fp.get_strings_starting_with("C:\\"))
    # print(fp.get_strings_ending_with(".rs"))
    # print(fp.get_strings_matching_regex("C:\\.*"))
    # print(fp.sanitize_ida_symbol_name("test.not.compatible-name"))
    # print(fp.set_comment_at_address(0x0045B116, "This is a test comment"))
    # print(fp.format_ea_t("0x0045B116"))
    # print(fp.format_internal_address_from_string("0x0045B116"))
    # print(fp.rename_symbol_at_address(0x0045B116, "test"))
    # print(fp.check_type_is(fp.format_internal_address_from_string("0x4721A0"), int))
    # print(fp.is_64_bit())
    # print(fp.get_all_xref_addresses_to_this_address(0x0045B116))
    # print(fp.dump_decompiled_function_as_text(0x456EB8))
    # for f in fp.walk_functions():
    #     print(fp.format_address(f))
    # print(fp.walk_functions_return_addresses())
    # print(fp.walk_functions_return_names())
    # print(fp.get_all_function_addresses_by_type(TYPE_FUNC_LIB))
    # print(fp.get_all_library_functions())
    # print(fp.get_all_lumina_functions())
    # print(fp.get_all_thunk_functions())
    # print(fp.rename_function(0x0045B116, "test"))
    # print(fp.reset_function_name(0x0045B116))
    # print(fp.get_function_address_from_name("test"))
    # print(fp.get_function_boundaries(0x0045B116))
    # print(fp.create_folder("TestFolder"))
    # print(fp.delete_folder("TestFolder"))
    # print(fp.move_to_folder("sub_41C780", "TestFolder"))
    # print(fp.check_folder_exists("TestFolder"))
    # print(fp.does_struct_exist("Rust_Slice"))
    # print(fp.set_symbol_type_to_custom_struct(0x45EDCC,"Rust_DebugInfo"))
    print(fp.get_all_imports())
except AttributeError as e:
    print(f"Error: {e}")
