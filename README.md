# FeatureProof

FeatureProof is an aspirational IDA Python common sense middleware library to build pseoducode-like scripts and plugins that resist the radical API shifts (and terrible design) of the IDAPython API.

It's designed to hotload functions as independent modules with multiple implementations and common interfaces. This allows for easy development, debugging, and testing of IDA Pro scripts and plugins with extensibility, compatibility, and maintainability in mind.

At this time, FeatureProof is a work in progress. The library is being parallel developed to support Project 0xA11c (Oxalic), with the intent of expanding its use to other projects in the future.

In its current version, FeatureProof enables IDAPython compatibility with IDA Pro v7.4-8.4. The intent is to expand that support to the new IDALIB API introduced with IDA 9. Backward compatibility with IDA 6.8-7.2 may be possible but not the main objective as it requires supporting Python 2.7 as well.

## Design Goals
- [✅] Autodetect IDA Pro version and transparently adjust the relevant function calls.
- [✅] List available functions and their compatibility status.
- [✅] Layout the functions in a modular fashion, using 'require()' hotloading to allow for easy development, debugging, and testing.
- [✅] Set a function template.
- [✅] Reach feature parity with FeatureProof beta.
- [✅] Keep a compatibility table for each function.
- [ ] Port function implementations to IDA 9 / IDALIB.
- [ ] Set a roadmap of desired functions.
- [ ] Consider GUI functions and ready plugin templating.
- [ ] Harvest atomic functions from existing scripts.

## Function Template
Create a new file in the Functions directory under the name 'function_name.py'. The file should contain the following template:

<Refer to sample_implementation/function_template.py>

The function will be loaded automatically and hotloaded upon changes in case of active development.

If functionality is added back to this repo, please add to the compatibility table along with relevant tested version compatibility.

# Usage
```python
    import idaapi
    idaapi.require("FeatureProof")
    from FeatureProof import Middleware

    fp = Middleware()
    try:
        print(fp.get_all_strings())
    except AttributeError as e:
        print(f"Error: {e}")
```

# Function Compatibility Table
- Updated 10.4.2024

### Core Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| format_address | ❌ | ✅ | ❌ |
| format_ea_t | ❌ | ✅ | ❌ |
| format_internal_address_from_string | ❌ | ✅ | ❌ |
| sanitize_ida_symbol_name | ❌ | ✅ | ❌ |
| rename_symbol_at_address | ❌ | ✅ | ❌ |
| check_type_is | ❌ | ✅ | ❌ |
| is_64_bit | ❌ | ✅ | ❌ |
### XREFs
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_xref_addresses_to_this_address | ❌ | ✅ | ❌ |
### Strings Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_all_strings| ❌ | ✅ | ❌ |
| get_strings_containing_substr | ❌ | ✅ | ❌ |
| get_strings_starting_with | ❌ | ✅ | ❌ |
| get_strings_ending_with | ❌ | ✅ | ❌ |
| get_strings_matching_regex | ❌ | ✅ | ❌ |
### Comment Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| set_comment_at_address | ❌ | ✅ | ❌ |
### Decompiler Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| dump_decompiled_function_as_text | ❌ | ✅ | ❌ |
### Function Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| walk_functions | ❌ | ✅ | ❌ |
| walk_functions_return_addresses | ❌ | ✅ | ❌ |
| walk_functions_return_names | ❌ | ✅ | ❌ |
| get_function_name_from_address | ❌ | ✅ | ❌ |
| get_all_library_functions | ❌ | ✅ | ❌ |
| get_all_lumina_functions | ❌ | ✅ | ❌ |
| get_all_thunk_functions | ❌ | ✅ | ❌ |
| rename_function | ❌ | ✅ | ❌ |
| reset_function_name | ❌ | ✅ | ❌ |
| get_function_boundaries | ❌ | ✅ | ❌ |
### Folder Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| create_folder | ❌ | ✅ | ❌ |
| delete_folder | ❌ | ✅ | ❌ |
| move_to_folder | ❌ | ✅ | ❌ |
| check_folder_exists | ❌ | ✅ | ❌ |
### Structure Functions
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| does_struct_exist | ❌ | ✅ | ❌ |
| set_symbol_type_to_custom_struct | ❌ | ✅ | ❌ |

# Tools currently relying on the FeatureProof Library:
- [Project 0xA11c (Oxalic)](https://github.com/juanandresgs/Proj-0xA11c)

# Roadmap (✅/❌)
- [✅] Implement hotloading logic
- [✅] Define a function template
- [✅] Publish development up to this point
- [✅] Break up monolithic functionality into templated functions
- [ NOT STARTED ] Refactor and test Project 0xA11c scripts to insure beta parity
- [ ] Deduplicate funtionality
- [ ] Is there a better organization/segmentation for functions by namespace or functionality type?
- [ ] Find a way to better integrate enums (function_types) and sub classes (func_info)

## Desired Functions:
- Get XREFs to symbol
- Get XREFs to address
- Get XREFs from address
- Get descending call graph from starting function
- Get ascending call graph from starting function
- Get XREF count to symbol
- def list_all_segments():
- def list_all_segments_by_name():
- def list_all_segments_by_starting_address():
- def determine_start_of_segment_at_address(ea):
- List functions in a specified folder in IDA Pro.
- def list_functions_in_folder(folder_name):
- def move_folder(src_folder_name, dest_folder_name):
- Move all functions from one folder to another in IDA Pro.
- def empty_folder(folder_name):
- Get all symbols referred to within a function
- Get all references to a given symbol name
- Get function at address
- Get segment name at address
- Get value of first operand
- Get value of second operand
- Get function argument values at XREFs
- Get symbol type
- def get_all_xref_addresses_to_this_name(symbol_name):
- def get_all_xrefs_from_within_function(ea):
- def get_all_xrefs_to_function(ea):
- def create_struct_type(struct_name, size, fields):
