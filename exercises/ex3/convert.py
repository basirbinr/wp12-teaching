import sys

BOHR_TO_ANGSTROM = 0.52917721092

def convert_coord_to_xyz(coord_file, xyz_file):
    atoms = []
    with open(coord_file, 'r') as f:
        for line in f:
            parts = line.split()
            # Look for lines with exactly 4 parts (x, y, z, element)
            # and ensure the first part is a number
            if len(parts) == 4 and "$" not in line:
                try:
                    x = float(parts[0]) * BOHR_TO_ANGSTROM
                    y = float(parts[1]) * BOHR_TO_ANGSTROM
                    z = float(parts[2]) * BOHR_TO_ANGSTROM
                    element = parts[3].capitalize()
                    atoms.append(f"{element} {x:12.8f} {y:12.8f} {z:12.8f}")
                except ValueError:
                    continue

    with open(xyz_file, 'w') as f:
        f.write(f"{len(atoms)}\n")
        f.write(f"Converted from {coord_file}\n")
        for atom in atoms:
            f.write(atom + "\n")
    print(f"Created {xyz_file}")

# Run the conversion
try:
    convert_coord_to_xyz("host/host_coord", "host/host.xyz")
    convert_coord_to_xyz("guest/guest_coord", "guest/guest.xyz")
    print("Conversion successful!")
except FileNotFoundError:
    print("Error: Could not find host_coord or guest_coord.")
    print("Make sure you are in the ex1.3 folder and the subfolders exist.")