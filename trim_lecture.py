# Import libraries
from PyPDF2 import PdfReader, PdfWriter
import os

# Define parameters
pdf_name = "lecture.pdf" # Name of the input pdf file
n = 35 # Number of pages
output_name = "lecture_trimmed.pdf" # Name of the output pdf file

# Open the input pdf file
pdf = PdfReader(pdf_name)

# Get the total number of pages in the pdf
total_pages = len(pdf.pages)

# Check if n is valid
if n > total_pages:
    print(f"Cannot remove {n} pages from a {total_pages}-page pdf.")
else:
    # Create a pdf writer object
    writer = PdfWriter()

    # Loop through the first n pages
    for i in range(n):
        # Get the page
        page = pdf.pages[i]

        # Add the page to the writer
        writer.add_page(page)

    # Open the output pdf file
    output = open(output_name, "wb")

    # Write the writer to the output file
    writer.write(output)

    # Close the output file
    output.close()

    # Print a confirmation message
    print(f"Saved {output_name} with {total_pages - n} pages.")
