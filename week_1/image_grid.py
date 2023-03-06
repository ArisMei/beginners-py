# import os.path
# new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_1"
# os.chdir(new_directory)
def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        # Reads content from the plaintext file
        with open(filename, "r") as file:
            # Read the first line for image dimensions
            try:
                line = file.readline().strip()
                # Here we obtain the width and height of the image
                width, height = map(int, line.split(","))
                #print(width, height)
            except (ValueError, IndexError):
                print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))
                return
            # Read the remaining lines for selected positions
            positions = set()
            for line in file:
                try:
                    x, y = map(int, line.strip().split(","))
                    positions.add((x, y))
                except (ValueError, IndexError):
                    print("Error in line: \"{}\"".format(line.strip()))
            
            # Print the image
            for y in range(height):
                for x in range(width):
                    if (x, y) in positions:
                        print(" ", end="")
                    else:
                        print("H", end="")
                print()

    # Deals with file reading exceptions
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))

main()
