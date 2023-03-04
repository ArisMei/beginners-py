def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        # Reads content from the plaintext file
        with open(filename, "r") as file:
        
            # Read all the lines in the file and store them to be printed in
            # the proper format. Remember to properly deal with incorrect lines.
            # (hint: arrays are a good choice of data structure)
        
        #
        # Print the image to the console here
        #
    
    # Deals with file reading exceptions
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))

main()