"""
Module: ppm converter
Autor: Ricardo Santinho Horta
Data: 08/12/2025
Description: Functions to convert PPM images from P6 (binary) format to P3 (ASCII), saving the result in a new "output.ppm" file.
"""
def converter(input_path):
    """
    Converts ppm6 to ppm3.
    
    :param input_path: ppm6 image path.
    """
    with open(input_path, 'rb') as f:
        print("\nconverter - def converter\nf Name in: " + f.name + " | Mode: " + f.mode)
        next(f)

        second_line = f.readline().strip().decode('utf-8')
        dimensions = [int(i) for i in second_line.split()]
        max_val = f.readline().strip().decode('utf-8')

        data = f.read()
        pixels_list = [list(data[i:i+3]) for i in range(0, len(data), 3)]
        write_file(dimensions, max_val, pixels_list)


def write_file(dimensions, max_val, pixels_list):
    """
    Saves the ppm3 file of the pixel list.

    :param dimensions: [width, height] of the image.
    :param max_val: maximum color value (usually 255).
    :param pixels_list: list of pixels in tuples [R,G,B].
    """
    with open("output.ppm", 'w') as f:
        print("\nconverter - def write_file\nf Name out: " + f.name + " | Mode: " + f.mode)
        f.write("P3\n" + str(dimensions[0]) + " " + str(dimensions[1]) + "\n" + max_val + "\n")
        
        counter = 0
        pixels_without_tuples = [num for pixel in pixels_list for num in pixel]
        for i in pixels_without_tuples:
            f.write(str(i) + " ")
            counter+=1
            if counter % 30 == 0:
                f.write("\n")
        print("\nfrom converter.write_file: <output.ppm> file created.")

