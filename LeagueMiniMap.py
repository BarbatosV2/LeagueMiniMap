from mss import mss
import cv2
import numpy as np

# Define the screen resolution (you can dynamically get this if needed)
screen_width = 2560  # Replace with your screen's actual width
screen_height = 1440  # Replace with your screen's actual height

# Define the region for the bottom-right corner (1080p size)
region = {
    "top": screen_height - 720,  # Y-coordinate (start from bottom)
    "left": screen_width - 1150, # X-coordinate (start from right)
    "width": 1920,  # Width of the capture area
    "height": 1080  # Height of the capture area
}

# Zoom factor (e.g., 1.2 means 20% zoom-in)
zoom_factor = 2.8

# Initialize the screen capture
with mss() as sct:
    while True:
        # Capture the screen
        screen = sct.grab(region)
        
        # Convert the image to a numpy array
        frame = np.array(screen)
        
        # Convert the BGRA image to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        
        # Crop the center of the frame for zoom effect
        height, width, _ = frame.shape
        crop_width = int(width / zoom_factor)
        crop_height = int(height / zoom_factor)
        start_x = (width - crop_width) // 2
        start_y = (height - crop_height) // 2
        cropped_frame = frame[start_y:start_y + crop_height, start_x:start_x + crop_width]
        
        # Resize the cropped frame back to the original size
        zoomed_frame = cv2.resize(cropped_frame, (width, height), interpolation=cv2.INTER_LINEAR)
        
        # Display the zoomed-in frame
        cv2.imshow("League Minimap", zoomed_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up
cv2.destroyAllWindows()
