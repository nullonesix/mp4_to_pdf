# Import libraries
import cv2
import numpy as np
import os
from tqdm import tqdm

# Define parameters
video_path = "lecture.mp4" # Path to the video file
output_dir = "slides" # Directory to save the slides
threshold = 0.99 # Similarity threshold to detect slide changes
frame_rate = 30 # Frame rate of the video

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the video
cap = cv2.VideoCapture(video_path)

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize variables
prev_frame = None # Previous frame
slide_count = 0 # Slide count

# Loop through the frames of the video with a step size of frame_rate
for frame_count in tqdm(range(0, total_frames, frame_rate)):
    # Set the current position of the video
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)

    # Read a frame
    ret, frame = cap.read()

    # Break if end of video
    if not ret:
        break

    # Resize the frame to a fixed width
    width = 800 * 2
    height = int(frame.shape[0] * width / frame.shape[1])
    frame = cv2.resize(frame, (width, height))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compare the current frame with the previous frame
    if prev_frame is not None:
        # Compute the normalized cross-correlation coefficient
        ncc = cv2.matchTemplate(gray, prev_frame, cv2.TM_CCOEFF_NORMED)[0][0]

        # If the coefficient is below the threshold, save the frame as a slide
        if ncc < threshold:
            slide_count += 1
            slide_name = f"slide_{slide_count:03d}.png"
            slide_path = os.path.join(output_dir, slide_name)
            cv2.imwrite(slide_path, frame)
            print(f"Saved {slide_name}")

    # Update the previous frame
    prev_frame = gray

# Release the video capture object
cap.release()

# Print the total number of slides
print(f"Total slides: {slide_count}")
