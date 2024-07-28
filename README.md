# Coordinates and RGB finder

## Overview
The Image Annotation Tool is a simple Python application that allows users to annotate images with labels and record the RGB values at specified points. This tool is useful for creating annotated datasets, marking significant points in images, and more. The annotations are saved in a JSON file, and the annotated image can also be saved.

## Features
- Click on an image to label points and record RGB values.
- Update labels for existing points.
- Save annotations as JSON and the annotated image as a JPEG.

## Installation

### Prerequisites
- Python 3.x
- OpenCV

### Installing OpenCV
To install the necessary libraries, use the following commands:

#### Using pip:
```bash
pip install opencv-python
pip install opencv-contrib-python  # For additional features
```

#### Using Conda:
```bash
conda install -c conda-forge opencv
```

## Usage

1. **Clone the Repository**: (if hosted on GitHub)
   ```bash
   git clone https://github.com/yourusername/image-annotation-tool.git
   cd image-annotation-tool
   ```

2. **Run the Script**:
   ```bash
   python annotate_image.py
   ```

3. **Annotate Image**:
   - **Left Mouse Click**: Add a label to the clicked point. Enter the label in the console when prompted.
   - **Shift + Left Mouse Click**: Update the label of the nearest point within a certain distance.
   - **Right Mouse Click**: Display the RGB values at the clicked point.

4. **Exit and Save**:
   - Press any key or close the image window to exit the program. Annotations and the image will be saved.

## File Descriptions

- `annotate_image.py`: The main script to run the annotation tool.
- `man.jpg`: Sample image used for annotation (replace with your image).
- `annotations.json`: Output file containing annotated points and labels.
- `annotated_image.jpg`: Output file of the annotated image.

## Future Enhancements
- Implement a graphical user interface (GUI) for better usability.
- Add functionality for drawing different shapes (e.g., bounding boxes, polygons).
- Enable exporting annotations in different formats (e.g., XML, CSV).

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## Acknowledgements
- This tool was built using the OpenCV library.
