# League Mini Map

For those who wants bigger Mini Map.

Is the mini map is so mini and want to zoom in the second screen?

This is it, this is the thing u want. 

This is the show case, I might add AI enemy detection later on. 

![FullSizeRender](https://github.com/user-attachments/assets/cd062e96-4812-4afd-bc21-987d615441e3)

# Edit according to your needs

I recommand you to edit these code region for your needs.

```
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
```

# Compile (.exe)

To make it as an app simply run this in the terminal or Windows PowerShell

First need to install pyinstaller

```
pip install pyinstaller
```
And then run
```
pyinstaller --onefile --windowed .\LeagueMiniMap.py
```

If windows detect as malware while in compile state, simply close the windows security system for awhile. 

Setting > Privacy & Security > Windows Security > Virus & threat protection > Virus & threat protection settings ... and simply turn off all for awhile. 

# NOTE

This is not a cheat software. Just a huge mini map xD.
