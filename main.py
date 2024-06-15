import ctypes
import os
import random

# Path to the folder containing wallpapers
folder_path = 'Your_Folder_Path'

# List all files in the folder
wallpapers = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Choose a random wallpaper
wallpaper = random.choice(wallpapers)

# Change the wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
