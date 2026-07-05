import argparse

def convert(value, from_unit, to_unit):
    # Basic unit conversion logic (example: length)
    if from_unit == 'm' and to_unit == 'ft':
        return value * 3.28084
    elif from_unit == 'ft' and to_unit == 'm':
        return value / 3.28084
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal Unit Converter")
    parser.add_argument("value", type=float, help="Value to convert")
    parser.add_argument("-f", "--from_unit", required=True, help="Source unit (e.g., m, ft)")
    parser.add_argument("-t", "--to_unit", required=True, help="Target unit (e.g., ft, m)")
    args = parser.parse_args()
    result = convert(args.value, args.from_unit, args.to_unit)
    print(f"{args.value} {args.from_unit} = {result:.4f} {args.to_unit}")