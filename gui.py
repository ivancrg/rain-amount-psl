# libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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
    else: latitude_label.configure(foreground="black") 

    if not is_number(longitude_entry.get()): 
        cnt += 1
        longitude_label.configure(foreground="red")
    else: longitude_label.configure(foreground="black")

    if not is_number(zoom_entry.get()): 
        cnt += 1
        zoom_label.configure(foreground="red")
    else: zoom_label.configure(foreground="black")

    return cnt == 0

def preview():
    if not check_entry(): return

    x, y, z, _ = map_utils.philamz_to_xyz(float(latitude_entry.get()), float(longitude_entry.get()), int(zoom_entry.get()))
    api_google_tile.getImage('tile.png', x, y, z, terrain_type.get(), 300, 300)

    img = Image.open('tile.png')
    # resize the image
    #resized_image = img.resize((300,300), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, image=new_image) 
    Tk.apdejt()

def calculate():
    if not check_entry(): return

    #value_label.config(text=str(worker.get_liters_per_hour(float(latitude_entry.get()), float(longitude_entry.get()), int(zoom_entry.get()), 15)))

    img = Image.open('tile.png')
    # resize the image
    #resized_image = img.resize((300,300), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, image=new_image) 
    Tk.updata()


# window and title
root = Tk()
root.title("Rain amount")

# main frame and window config
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(340, 590)
root.maxsize(340, 590)

# latitude label and edit box
latitude_label = ttk.Label(mainframe, text='Latitude')
latitude_label.grid(column=1, row=0)
latitude = StringVar()
latitude_entry = ttk.Entry(mainframe, width=11, textvariable=latitude)
latitude_entry.grid(column=1, row=1)

# longitude label and edit box
longitude_label = ttk.Label(mainframe, text='Longitude')
longitude_label.grid(column=2, row=0)
longitude = StringVar()
longitude_entry = ttk.Entry(mainframe, width=11, textvariable=longitude)
longitude_entry.grid(column=2, row=1)

# zoom label and edit box
zoom_label = ttk.Label(mainframe, text='Zoom level')
zoom_label.grid(column=3, row=0)
zoom = StringVar()
zoom_entry = ttk.Entry(mainframe, width=11, textvariable=zoom)
zoom_entry.grid(column=3, row=1)

terrain_type = StringVar(mainframe, 't')
Radiobutton(mainframe, text="Terrain", variable=terrain_type, value='t').grid(column=2, row=3, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Satelite", variable=terrain_type, value='s').grid(column=2, row=4, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Hybrid", variable=terrain_type, value='y').grid(column=2, row=5, sticky=W, padx=(25, 0))
Radiobutton(mainframe, text="Map", variable=terrain_type, value='m').grid(column=2, row=6, sticky=W, padx=(25, 0))


# preview button
ttk.Button(mainframe, text='Preview', command=preview).grid(column=2, row=7, pady=6)

# image preview
canvas = Canvas(mainframe, width=300, height=300)      
canvas.grid(column=1, row=8, columnspan=3)     
#img = Image.open("s.png")
# resize the image
#resized_image = img.resize((300,300), Image.ANTIALIAS)
#new_image = ImageTk.PhotoImage(resized_image)
#canvas.create_image(10, 10, image=new_image)  

# calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=9, pady=12)

value_headline_label = ttk.Label(mainframe, text='Amount of rain(L):')
value_headline_label.grid(column=2, row=10)
value_label = ttk.Label(mainframe, text='12 L')
value_label.grid(column=2, row=11)

root.mainloop()