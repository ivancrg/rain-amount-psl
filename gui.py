from ctypes import alignment
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk

import api_rainviewer
import api_google_tile
import map_utils
import worker


def is_number(s):
    if len(s) == 0:
        return False

    for i in range(len(s)):
        if s[i] not in '0123456789.+-':
            return False

    return True


def check_entry():
    cnt = 0

    if not is_number(latitude_entry.get()):
        cnt += 1
        latitude_label.configure(foreground="red")
    else:
        latitude_label.configure(foreground="black")

    if not is_number(longitude_entry.get()):
        cnt += 1
        longitude_label.configure(foreground="red")
    else:
        longitude_label.configure(foreground="black")

    if not is_number(zoom_entry.get()):
        cnt += 1
        zoom_label.configure(foreground="red")
    else:
        zoom_label.configure(foreground="black")

    return cnt == 0


def preview():
    if not check_entry():
        return
    
    x, y, z, _ = map_utils.philamz_to_xyz(float(latitude_entry.get()), float(
        longitude_entry.get()), int(zoom_entry.get()))
    
    if terrain_type.get() == "r":
        api_rainviewer.getImage("preview.png", x, y, z)
    else:
        api_google_tile.getImage('preview.png', x, y, z, terrain_type.get(), 300, 300)

    img = Image.open('preview.png')
    new_image = ImageTk.PhotoImage(img)
    canvas.create_image(150, 150, image=new_image)
    Tk.update()


def calculate():
    if not check_entry():
        return

    value_label.config(
        text=f"{str(round(worker.get_liters_per_hour(float(latitude_entry.get()), float(longitude_entry.get()), int(zoom_entry.get()), 15) / 1000.0))} m³/h")

    preview()


# Window and title
root = Tk()
root.title("Rain amount")

# Main frame and window config
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(355, 625)
root.maxsize(355, 625)

# Latitude label and edit box
latitude_label = ttk.Label(mainframe, text='Latitude')
latitude_label.grid(column=1, row=0)
latitude = StringVar()
latitude_entry = ttk.Entry(mainframe, width=11, textvariable=latitude)
latitude_entry.grid(column=1, row=1)

# Longitude label and edit box
longitude_label = ttk.Label(mainframe, text='Longitude')
longitude_label.grid(column=2, row=0)
longitude = StringVar()
longitude_entry = ttk.Entry(mainframe, width=11, textvariable=longitude)
longitude_entry.grid(column=2, row=1)

# Zoom label and edit box
zoom_label = ttk.Label(mainframe, text='Zoom level')
zoom_label.grid(column=3, row=0)
zoom = StringVar()
zoom_entry = ttk.Entry(mainframe, width=11, textvariable=zoom)
zoom_entry.grid(column=3, row=1)

terrain_type = StringVar(mainframe, 't')
Radiobutton(mainframe, text="Terrain", variable=terrain_type,
            value='t').grid(column=2, row=3, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Satelite", variable=terrain_type,
            value='s').grid(column=2, row=4, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Hybrid", variable=terrain_type,
            value='y').grid(column=2, row=5, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Map", variable=terrain_type, value='m').grid(
    column=2, row=6, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Radar", variable=terrain_type, value='r').grid(
    column=2, row=7, sticky=W, padx=(25, 0))


# Preview button
ttk.Button(mainframe, text='Preview', command=preview).grid(
    column=2, row=8, pady=6)

# Image preview
canvas = Canvas(mainframe, width=300, height=300)
canvas.grid(column=1, row=9, columnspan=3)

# Calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=2, row=10, pady=12)

value_headline_label = ttk.Label(mainframe, text='Amount of rain (m³/h):')
value_headline_label.grid(column=2, row=11)
value_label = ttk.Label(mainframe, text='-')
value_label.configure(anchor="center")
value_label.grid(column=2, row=12)

root.mainloop()
