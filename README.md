# Dominant Color Extractor

The Dominant Color Extractor is a simple Python application that allows you to extract the dominant color from an image file. It provides a user-friendly graphical interface built with CustomTkinter, making it easy for anyone to use.

## Features

- Select an image file (supports JPG, JPEG, and PNG formats).
- Extract the dominant color from the selected image.
- Display the RGB value of the dominant color.
- View the dominant color as a color swatch.

## Requirements

Before using the Dominant Color Extractor, make sure you have the following dependencies installed:

- Python 3.x
- CustomTkinter (a custom-themed Tkinter library)
- Matplotlib (for displaying the color swatch)
- ColorThief (for extracting the dominant color from the image)

You can install the required dependencies using pip:

```bash
pip install customtkinter matplotlib colorthief
```

## How to Use

1. Clone this repository or download the source code.
2. Ensure you have the required dependencies installed (see the "Requirements" section above).
3. Run the `dce.py` script.

   ```bash
   python dce.py
   ```

4. Click the "Select Image" button to choose an image file.
5. The program will extract the dominant color from the image and display it as an RGB value.
6. You will also see a color swatch representing the dominant color.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- 0xRezoc

## Acknowledgments

- [CustomTkinter](https://customtkinter.tomschimansky.com/)
- [Matplotlib](https://matplotlib.org/)
- [ColorThief](https://github.com/fengsp/color-thief-py)

