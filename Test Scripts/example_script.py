import idaapi
idaapi.require("FeatureProof")
from FeatureProof import Middleware

fp = Middleware("sample_implementation")

# Access and execute the example function for the current IDA Pro version
try:
    print("Equivalence setup")
    example_function = fp.function_template
    print("Executing function")
    example_function()
except AttributeError as e:
    print(f"Error: {e}")
