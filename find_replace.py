import sys

def process_gcode(gcode_file):
    """Modifies the G-code file by:
    1. Replacing all occurrences of 'X-Find-X' with 'X-Replace-X' to comment them out.
    """

    # Read the original G-code file
    with open(gcode_file, "r") as file:
        lines = file.readlines()

    # Step 1: Find all occurrences of 'X-Find-X' and replace with 'X-Replace-X'
    modified_lines = [line.replace("X-Find-X", "X-Replace-X") for line in lines]

    # Write the modified G-code back to the file
    with open(gcode_file, "w") as file:
        file.writelines(modified_lines)

    print(f"Processed {gcode_file}: 'X-Find-X' commented out.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_gcode.py <gcode_file>")
    else:
        process_gcode(sys.argv[1])
