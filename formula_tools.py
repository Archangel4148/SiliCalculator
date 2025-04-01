import re

import periodictable


def validate_formula(formula: str) -> tuple[bool, list | None]:
    """Check that the provided chemical formula is valid"""
    # Make sure string format is valid
    element_pattern = r"[A-Z][a-z]?"
    invalid_pattern = r"[a-z][a-z]"
    invalid_string = re.findall(invalid_pattern, formula)
    if invalid_string:
        return False, None

    # Extract each symbol from the input string
    element_strings = re.findall(element_pattern, formula)
    result_list = []

    # Check each symbol using periodictable
    for element in element_strings:
        if hasattr(periodictable, element):
            result_list.append(element)
        else:
            return False, None
    return True, result_list


def extract_coefficients(formula: str) -> list:
    """Extract coefficients for each symbol in a formula (1 for symbols without coefficients)"""

    # Regular expression to split elements and coefficients into groups:
    # ( single element? , regular coefficient? , parenthesis group? , parenthesis coefficient? )
    pattern = r'([A-Z][a-z]?)(\d*\.?\d*)|\(([^)]+)\)(\d*)'
    matches = re.findall(pattern, formula)

    # Extract the coefficients, handling each regex group
    coefficients = []
    for match in matches:
        if match[0]:  # Single element
            coefficient = float(match[1]) if match[1] else 1.0
            coefficients.append(coefficient)
        elif match[2]:  # Parenthesis group
            # For parenthesis groups, extract them as a separate formula
            group_coefficients = extract_coefficients(match[2])
            multiplier = float(match[3]) if match[3] else 1.0
            for coeff in group_coefficients:
                coefficients.append(coeff * multiplier)

    return coefficients


if __name__ == '__main__':
    # Validate the provided formula and extract its coefficients
    compound = 'Mg2.5(OH)2(NN)'
    _, symbols = validate_formula(compound)
    coefficients = extract_coefficients(compound)
    print("Symbols:", symbols)
    print("Coefficients:", coefficients)
