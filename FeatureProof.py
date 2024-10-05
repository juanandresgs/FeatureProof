"""
    FeatureProof Middleware for IDAPython cross-compatibility
"""
import idaapi
import sys
import os
import importlib.util
import logging

class Middleware:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Middleware, cls).__new__(cls)
        return cls._instance

    def __init__(self, folder_path='Functions'):
        if not Middleware._initialized:
            self.folder_path = os.path.join(os.path.dirname(__file__), folder_path)
            self.functions = {}
            self.module_globals = {}
            self.setup_logger()
            self.get_ida_version()
            self.inject_imports()
            self.load_modules()
            Middleware._initialized = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Middleware()
        return cls._instance

    def setup_logger(self):
        self.logger = logging.getLogger('FeatureProof')
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.WARNING)
        self.module_globals['logger'] = self.logger

    def set_debug_mode(self, debug_mode):
        if debug_mode:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

    def set_logging_level(self, level):
            self.logger.setLevel(level)

    def get_ida_version(self):
        self.version = idaapi.get_kernel_version()
        major_version = int(self.version.split('.')[0])
        minor_version = int(self.version.split('.')[1])
        if (major_version == 6 and minor_version >= 8) or (major_version == 7 and minor_version <= 3):
            self.version_enum = 6
        elif (major_version == 7 and minor_version >= 4) or (major_version == 8):
            self.version_enum = 8
        elif major_version == 9:
            self.version_enum = 9
        else:
            self.logger.error(f"Unsupported IDA Pro version: {self.version}")
            sys.exit(f"Unsupported IDA Pro version: {self.version}")

    def inject_imports(self):
        modules = [
            'idaapi', 'idc', 'idautils', 'ida_struct', 'ida_funcs',
            'ida_segment', 'ida_xref', 'ida_bytes', 'ida_typeinf', 'ida_dirtree', 'ida_hexrays', 'ida_lines', 'os', 're'
        ]
        for module_name in modules:
            module = idaapi.require(module_name)
            if module is None:
                try:
                    module = __import__(module_name)
                except ImportError as e:
                    self.logger.error(f"Error importing {module_name}: {e}")
                    continue
            self.module_globals[module_name] = module
            self.logger.debug(f"Injected {module_name}: {module}")

    def load_modules(self):
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                module_path = os.path.join(self.folder_path, filename)
                self.hotload_module(module_name, module_path)

    def hotload_module(self, module_name, module_path):
        if not os.path.isfile(module_path):
            return

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec is None:
            return

        module = importlib.util.module_from_spec(spec)
        if spec.loader is None:
            return

        # Update the module's global namespace with module_globals and functions
        module.__dict__.update(self.module_globals)
        module.__dict__.update(self.functions)
        module.__dict__['fp'] = self

        spec.loader.exec_module(module)

        # Debugging: Print the module's globals to verify imports
        self.logger.debug(f"Module {module_name} globals: {module.__dict__.keys()}")

        if hasattr(module, 'get_function'):
            func_info = module.get_function()
            self.update_function(module_name, func_info)

    def update_function(self, module_name, func_info):
        if self.version_enum in func_info:
            self.functions[module_name] = func_info[self.version_enum]['implementation']
            self.logger.info(f"Function {module_name} loaded for version {self.version_enum}")
        else:
            self.logger.warning(f"Function {module_name} not available for version {self.version_enum}")

    def __getattr__(self, name):
        if name in self.functions:
            return self.functions[name]
        if name in self.module_globals:
            return self.module_globals[name]
        raise AttributeError(f"'Middleware' object has no attribute '{name}'")
