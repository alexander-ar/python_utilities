import os
import sys
from PIL import Image

def JPGtoPNGconverter():
    '''
    This function takes a folder path as a first argument and converts all the JPG files inside to PNG format
    and saves the new images in the output folder, which is provided as a second argument.
    This script can be run from a command line, for example:
    > cd path_to_script_directory
    > python3 JPGtoPNGconverter.py input_folder_path output_folder_path
    '''
    print("The JPG to PNG converter program is running...")
    # check if both arguments are provided in the terminal after the module name
    assert len(sys.argv)==3, "Please add first argument as path to folder with JPEG images and second argument as path to the folder for output PNG images"

    # grab both folder destinations from the input arguments in the terminal.  Return error and terminate the program if
    # input folder does not exist. Create new output folder if one does not exist
    input_folder = sys.argv[1]
    if os.path.exists(input_folder):
        print(f"{input_folder} is a valid path")
    else:
        print(f"{input_folder} is not a valid path. Please provide a valid path to the folder with JPEG images for conversion")
        raise ValueError("Ending the program...")

    output_folder = sys.argv[2]
    if os.path.exists(output_folder):
        print(f"{output_folder} is a valid path. Proceeding with file conversion...")
    else:
        print(f"{output_folder} does not exist. Creating a new folder for output PNG images")
        os.makedirs(output_folder)


    # loop through the input folder, make a list with all JPEG files names for conversion
    jpeg_files = [file for file in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file)) \
                  and file.endswith(".jpg")]

    # convert images to PNG and save to the new folder
    png_files = []
    for file in jpeg_files:
        full_file_path = os.path.join(input_folder, file)
        img = Image.open(full_file_path)
        new_file_name = file.replace(".jpg", ".png")
        full_output_file_path = os.path.join(output_folder, new_file_name)
        try:
            img.save(full_output_file_path)
            png_files.append(new_file_name)
        except:
            print(f"Could not convert file {file} to PNG format")

    print(f"The following files were saved in PNG format:")
    for file in png_files:
        print(file)



JPGtoPNGconverter()
