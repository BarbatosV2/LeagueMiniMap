# League Mini Map

For those who wants bigger Mini Map.

Is the mini map is so mini and want to zoom in the second screen?

This is it, this is the thing u want. 

This is the show case, I might add AI enemy detection later on. 

![FullSizeRender - Copy](https://github.com/user-attachments/assets/84c73a73-2b95-49e4-99ce-3cf33b1c86ea)


# Application Download Link

[[Rampardos/LeagueMiniMap](https://huggingface.co/Rampardos/LeagueMiniMap/tree/main)]  (Hugging Face Link)

# Edit according to your needs

I recommand you to edit these code region for your needs.

```
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

# Monitor Orientation Usage
1. The best way

![monitor orientation 1](https://github.com/user-attachments/assets/83d8534c-3fbb-4782-a72a-013cad34b312)

2. Second best way

![monitor orientation 2](https://github.com/user-attachments/assets/8f3c4fd2-09ed-4019-8bd8-441adf7a68be)

I do not recommand putting on the second monitor on the left side, as might be more distracting and too much turining head around.

As long as League MiniMap and Zoom in MiniMap closer, the better it will be. 

# NOTE

This is not a cheat software. Just a huge mini map xD.
