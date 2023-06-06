# Import libraries
from PIL import Image
import os
from tqdm import tqdm

# Define parameters
output_dir = "slides" # Directory where the slides are saved
pdf_name = "lecture.pdf" # Name of the output pdf file

# Get the list of jpg files in the output directory
jpg_files = [f for f in os.listdir(output_dir) if f.endswith(".png")]

# Sort the jpg files by name
jpg_files.sort()

# Initialize an empty list to store the images
images = []

# Loop through the jpg files
for jpg_file in tqdm(jpg_files):
    # Open the image
    image = Image.open(os.path.join(output_dir, jpg_file))

    # Convert the image to RGB mode
    image = image.convert("RGB")

    # Append the image to the list
    images.append(image)

# Save the first image as a pdf and add the rest as pages
images[0].save(pdf_name, save_all=True, append_images=images[1:])

# Print a confirmation message
print(f"Saved {pdf_name}")
