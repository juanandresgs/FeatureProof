"""
    FeatureProof Middleware function: get_regex_matches_from_strings.py

    Get portion of strings that match a given regex pattern.

    :param pattern: The regex pattern to filter strings.
    :param min_length: The minimum length of the strings to retrieve.
    :return: List of tuples containing (address, match).
"""
import re
filename = os.path.splitext(os.path.basename(__file__))[0][:-3]
logger = fp.logger

def function_6():
    logger.debug(f"{filename} for IDA Pro 6.8-7.x called successfully!")

def function_8(pattern, min_length=4):
    logger.debug(f"{filename} for IDVA Pro 7.x-8.4 called successfully!")
    regex = re.compile(pattern)
    matches = []
    for addr, s in fp.get_all_strings(min_length):
        match = regex.findall(s)
        if match:
            matches.extend([(addr, m) for m in match])
    return matches

def function_9():
    logger.debug(f"{filename} for IDA Pro 9+ called successfully!")

def get_function():
    logger.debug(f"{filename} hotloaded successfully!")
    return {
        8: {
            'implementation': function_8,
            'description': 'Retrieve all strings in the binary that match the given regex pattern and with a minimum length.',
            'parameters': ['pattern', 'min_length'],
            'return_type': 'List[Tuple[int, str]]'
        },
    }
