from formula_tools import validate_formula


def get_component_count():
    """Get user input for number of glass components"""
    while True:
        # Input validation
        try:
            component_count = int(input("How many components does your glass have? "))
            if 1 <= component_count <= 10:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter an integer between 1 and 10 ")

    # Grammar for plural
    if component_count == 1:
        print("Your glass has 1 component")
    else:
        print("Your glass has " + str(component_count) + " components")
    return component_count


def get_glass_components(component_count: int):
    """Collect and validate glass components from the user"""
    glass_components = []
    for i in range(component_count):
        while True:
            component = input(f"Glass component {str(i + 1)}: ")
            if validate_formula(component)[0]:
                glass_components.append(component)
                break
            else:
                print(f"Invalid component \'{component}\', try again...")

    print(f"Glass components: {glass_components}\n")
    return glass_components


def get_raw_materials(count: int, glist: list):
    """Collect and validate raw materials from the user"""
    raw_materials = []
    for i in range(count):
        while True:
            try:
                # Get the material formula and add it to the list
                material = input("Raw material for " + glist[i] + ": ")
                if validate_formula(material)[0]:
                    raw_materials.append(material)
                    break
            except ValueError:
                print("Not a valid material, please try again.")

    # Display the provided raw materials
    print("\n=== Raw Materials ===")
    for x in raw_materials:
        print(f"For {glist[raw_materials.index(x)]}: {x}")
    check = input("Are these correct? (y/n): ")
    if check.casefold() != "y":
        get_raw_materials(count, glist)

    return raw_materials


def get_mole_percent(components):
    components = components
    mole_percents = []
    for component in components:
        while True:
            # Input validation
            try:
                percent = float(input(f"What mol% of {component}? "))
                mole_percents.append(percent)
                break
            except ValueError:
                print("Please enter a number between 0 and 100 ")

    # Get mole percent total
    total_mole_percent = sum([float(percent) for percent in mole_percents])

    if total_mole_percent != 100:
        print("Mol% total doesn't equal 100.")
        get_mole_percent(components)
    else:
        # Display the mole percent values
        print("\n=== Mol% Inputs ===")
        for x in components:
            index = components.index(x)
            print(f"{x}: {mole_percents[index]}%")
        check = input("Are these correct? (y/n): ")
        if check.casefold() != "y":
            get_mole_percent(components)
        print()
        return mole_percents


# def mass_from_symbol(symbol: str):
#     """Get elemental mass from symbol"""
#     element = getattr(periodictable, symbol)
#     return element.mass


if __name__ == "__main__":
    # Get component count, component list, mole percents, and raw materials
    component_count = get_component_count()
    glass_components = get_glass_components(component_count)
    mole_percents = get_mole_percent(glass_components)
    raw_materials = get_raw_materials(component_count, glass_components)
