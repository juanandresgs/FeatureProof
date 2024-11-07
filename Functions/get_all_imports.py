"""
    FeatureProof Middleware function: get_all_imports.py

    Get all imports from the current binary.

    :return: list of function names and address
"""
import os
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6(): # Add parameters as needed
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")
    # Implementation for IDA Pro 6.8-7.x

def function_8(): # Add parameters as needed
    logger.debug(f"{filename} for IDA Pro 7.x-8.4 called successfully!")
    imports = []
    for i in range(idaapi.get_import_module_qty()):
        module_name = idaapi.get_import_module_name(i)
        if module_name:
            logger.debug(f"Module: {module_name}")
            def callback(ea, name, ordinal):
                import_entry = (name or f'ordinal #{ordinal}', ea)
                imports.append(import_entry)
                logger.debug(f"  {ea:08X}: {import_entry[0]}")
                return True
            idaapi.enum_import_names(i, callback)
    return imports

def function_9(): # Add parameters as needed
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")
    # Implementation for IDA Pro 9+

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Get all imports from the current binary.',
            'return_type': 'list of function names and address'
        },
    }
