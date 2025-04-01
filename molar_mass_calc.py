from collections import defaultdict

import periodictable

from formula_tools import validate_formula, extract_coefficients


def calculate_molar_mass(compound: str, verbose=False) -> float:
    # Validate formula strings
    valid, result_list = validate_formula(compound)
    if not valid:
        raise ValueError(f"Invalid formula provided: \'{compound}\'")

    # Collect valid elements and coefficients
    elements = [symbol for symbol in result_list if hasattr(periodictable, symbol)]
    coefficients = extract_coefficients(compound)

    # Clean up the lists, combining duplicate symbols and their coefficients
    element_totals = defaultdict(float)
    for element, coefficient in zip(elements, coefficients):
        element_totals[element] += coefficient
    clean_elements = list(element_totals.keys())
    clean_coefficients = list(element_totals.values())

    # Calculate the total masses for each element (periodic table mass * coefficient)
    total_masses = [getattr(periodictable, element).mass * coefficient for element, coefficient in
                    zip(clean_elements, clean_coefficients)]

    if verbose:
        # Print the parsed values and totals (if running in verbose mode)
        print("Elements:", clean_elements)
        print("Coefficients:", clean_coefficients)
        print("Element Total Masses:", total_masses)

    # The molar mass of the compound is the sum of the molar masses of each element
    return sum(total_masses)


if __name__ == '__main__':
    # Example formulas to demonstrate functionality
    test_formulas = [
        "H2",
        "O2",
        "H2O",
        "CO2",
        "NaCl",
        "C6H12O6",
        "NaOH",
        "Ca(OH)2",
        "Al2(SO4)3",
        "Fe(OH)3",
        "CuSO4·5H2O",
        "Mg2.5(OH)2(NN)",
        "K3[Fe(CN)6]",
        "Na3PO4",
        "C100H200O100",
    ]

    # Calculate and print the molar mass for each compound (rounding to prevent floating point errors)
    for f in test_formulas:
        print(f"\nMolar Mass of {f}: {round(calculate_molar_mass(f), 10)} g/mol")
