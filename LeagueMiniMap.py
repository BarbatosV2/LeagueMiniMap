from mss import mss
import cv2
import numpy as np
from screeninfo import get_monitors

# Get the primary monitor's resolution
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

# Define the region for the bottom-right corner (1080p size)
region = {
    "top": screen_height - 728,  # Y-coordinate (start from bottom)
    "left": screen_width - 1145, # X-coordinate (start from right)
    "width": 1920,  # Width of the capture area
    "height": 1080  # Height of the capture area
}

# Zoom factor (e.g., 1.2 means 20% zoom-in)
zoom_factor = 2.9

# Create a named window with resizable and aspect ratio preservation option
cv2.namedWindow("League Minimap", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

# Initialize the screen capture
with mss() as sct:
    while True:
        # Capture the screen
        screen = sct.grab(region)
        
        # Convert the image to a numpy array
        frame = np.array(screen)
        
        # Convert the BGRA image to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        
        # Determine the smaller dimension for the square crop
        height, width, _ = frame.shape
        square_size = int(min(width, height) / zoom_factor)
        
        # Calculate the starting coordinates for the crop
        start_x = (width - square_size) // 2
        start_y = (height - square_size) // 2
        
        # Crop the square region
        cropped_frame = frame[start_y:start_y + square_size, start_x:start_x + square_size]
        
        # Resize the cropped frame to fit the original window's size
        zoomed_frame = cv2.resize(cropped_frame, (square_size, square_size), interpolation=cv2.INTER_LINEAR)
        
        # Display the zoomed-in frame
        cv2.imshow("League Minimap", zoomed_frame)
        
        # Check if 'q' is pressed or if the window is closed
        if cv2.waitKey(1) & 0xFF == ord('?') or cv2.getWindowProperty("League Minimap", cv2.WND_PROP_VISIBLE) < 1:
            break

# Clean up
cv2.destroyAllWindows()
