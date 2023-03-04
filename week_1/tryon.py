import os
new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_1"
os.chdir(new_directory)

def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        # Reads content from the plaintext file
        with open(filename, "r") as file:
            # Read the first line to get the image dimensions
            dimensions = file.readline().strip().split(',')
            width = int(dimensions[0])
            height = int(dimensions[1])
            # Create a 2D array with dimensions given in the file
            image = [['H' for j in range(width)] for i in range(height)]
            # Read the remaining lines and set the selected positions to ' '
            for line in file:
                try:
                    x, y = map(int, line.strip().split(','))
                    if x < height and y < width:
                        image[x][y] = ' '
                except ValueError:
                    print("Invalid line format:", line.strip())

            # Print the resulting image
            for row in image:
                print(''.join(row))

    # Deals with file reading exceptions
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))

main()

