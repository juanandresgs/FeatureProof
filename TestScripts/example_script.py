import idaapi
idaapi.require("FeatureProof")
from FeatureProof.FeatureProof import Middleware

fp = Middleware("./TestScripts/sample_implementation") # Custom implementations folder
fp.set_debug_mode(True)

# Access and execute the example function for the current IDA Pro version
try:
    print("Equivalence setup")
    example_function = fp.function_template
    print("Executing function")
    example_function()
except AttributeError as e:
    print(f"Error: {e}")
