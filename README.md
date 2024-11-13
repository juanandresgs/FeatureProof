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
- Updated 11.13.2024

### Core
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| format_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| format_ea_t | ❌ | ✅ | ❌ | ❌ | ❌ |
| format_internal_address_from_string | ❌ | ✅ | ❌ | ❌ | ❌ |
| sanitize_ida_symbol_name | ❌ | ✅ | ❌ | ❌ | ❌ |
| is_64_bit | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_imagebase | ❌ | ✅ | ❌ | ❌ | ❌ |

### Memory and Data
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_bytes_at_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_byte | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_qword_at_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_dword_at_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_wide_dword | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_wide_word | ❌ | ✅ | ❌ | ❌ | ❌ |

### Instructions and Operations
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_all_instructions | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_instruction | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_next_instruction_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_previous_instruction_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_operand_type | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_operand_value | ❌ | ✅ | ❌ | ❌ | ❌ |

### Functions and Names
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| walk_functions | ❌ | ✅ | ❌ | ❌ | ❌ |
| walk_functions_return_addresses | ❌ | ✅ | ❌ | ❌ | ❌ |
| walk_functions_return_names | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_function_name_from_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_function_address_from_name | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_all_library_functions | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_all_lumina_functions | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_all_thunk_functions | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_all_function_addresses_by_type | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_function_boundaries | ❌ | ✅ | ❌ | ❌ | ❌ |
| rename_function | ❌ | ✅ | ❌ | ❌ | ❌ |
| reset_function_name | ❌ | ✅ | ❌ | ❌ | ❌ |

### References and Cross-References
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_all_xref_addresses_to_this_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_all_imports | ❌ | ✅ | ❌ | ❌ | ❌ |

### Strings
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_all_strings | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_strings_containing_substr | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_strings_starting_with | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_strings_ending_with | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_strings_matching_regex | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_regex_matches_from_strings | ❌ | ✅ | ❌ | ❌ | ❌ |

### Structures and Types
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| does_struct_exist | ❌ | ✅ | ❌ | ❌ | ❌ |
| create_new_struct | ❌ | ✅ | ❌ | ❌ | ❌ |
| check_if_struct_exists | ❌ | ✅ | ❌ | ❌ | ❌ |
| set_symbol_type_to_custom_struct | ❌ | ✅ | ❌ | ❌ | ❌ |
| check_type_is | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_symbol_type | ❌ | ✅ | ❌ | ❌ | ❌ |

### Segments
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| get_segment_by_name | ❌ | ✅ | ❌ | ❌ | ❌ |
| get_segment_name_at_address | ❌ | ✅ | ❌ | ❌ | ❌ |

### Organization
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| create_folder | ❌ | ✅ | ❌ | ❌ | ❌ |
| delete_folder | ❌ | ✅ | ❌ | ❌ | ❌ |
| move_to_folder | ❌ | ✅ | ❌ | ❌ | ❌ |
| check_folder_exists | ❌ | ✅ | ❌ | ❌ | ❌ |

### Comments and Decompilation
| Function Name | IDA 6.8-7.2 | IDA 7.3-8.4 | IDA 9.0+ | Binja | Ghidra |
|---------------|-------------|-------------|----------|-------| ------ |
| set_comment_at_address | ❌ | ✅ | ❌ | ❌ | ❌ |
| dump_decompiled_function_as_text | ❌ | ✅ | ❌ | ❌ | ❌ |

# Tools currently relying on the FeatureProof Library:
- [Project 0xA11c (Oxalic)](https://github.com/juanandresgs/Proj-0xA11c)

# Roadmap (✅/❌)
- [✅] Implement hotloading logic
- [✅] Define a function template
- [✅] Publish development up to this point
- [✅] Break up monolithic functionality into templated functions
- [✅] Find a way to better integrate enums (function_types) and sub classes (func_info)
- [🚧] Refactor and test Project 0xA11c scripts to insure beta parity
- [ ] Assess the viability of reimplementing the main harness for Binary Ninja
- [ ] Assess the viability of reimplementing the main harness for Ghidra
- [ ] Can we enable autocompletion from scripts that rely on FeatureProof?

## Desired Functions:
- Get ascending call graph from starting function
- Get descending call graph from starting function
- Get XREF count to symbol
- def list_all_segments_by_name():
- def list_all_segments_by_starting_address():
- def determine_start_of_segment_at_address(ea):
- List functions in a specified folder in IDA Pro.
- def list_functions_in_folder(folder_name):
- def move_folder(src_folder_name, dest_folder_name):
- Move all functions from one folder to another in IDA Pro.
- def empty_folder(folder_name):
- Get all symbols referred to within a function
- Get function argument values at XREFs
- def get_all_xrefs_from_within_function(ea):
- def create_struct_type(struct_name, size, fields):
