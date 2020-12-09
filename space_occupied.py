# program that for a given folder calculates the total space that it occupies
import os

def space_occupied(path):
    # Initialize total_size variable
    total_size = 0

    # For every item in the directory
    for sub_path in os.listdir(path):
        #Create the new complete path of the item by concatenating old path + item name
        new_path = os.path.join(path, sub_path)

        # If file add to total_size
        if os.path.isfile(new_path):
            total_size += os.path.getsize(sub_path)

        # If directory, call space_occupied function with new folder recursively and add to total size
        else:
            total_size += space_occupied(new_path)

    # Return result in Bytes
    return total_size

# IMPORTANT: Path must be given as a raw string
# Optional: Divide result by 1000 to get result in KB instead of B
print("Space Occupied: {} KB".format(space_occupied(r'C:Here\Goes\Your\Path')/1000))
