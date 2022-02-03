# libraries
from tkinter import *
from tkinter import ttk
# pip install Pillow
from PIL import Image, ImageTk

# window and title
root = Tk()
root.title("Rain amount")

# main frame and window config
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(340, 450)
root.maxsize(340, 450)

# latitude label and edit box
ttk.Label(mainframe, text='Latitude').grid(column=1, row=0)
latitude = StringVar()
latitude_entry = ttk.Entry(mainframe, width=11, textvariable=latitude)
latitude_entry.grid(column=1, row=1)

# longitude label and edit box
ttk.Label(mainframe, text='Longitude').grid(column=2, row=0)
longitude = StringVar()
longitude_entry = ttk.Entry(mainframe, width=11, textvariable=longitude)
longitude_entry.grid(column=2, row=1)

# zoom label and edit box
ttk.Label(mainframe, text='Zoom level').grid(column=3, row=0)
zoom = StringVar()
zoom_entry = ttk.Entry(mainframe, width=11, textvariable=zoom)
zoom_entry.grid(column=3, row=1)

# preview button
# TODO command=
ttk.Button(mainframe, text='Preview').grid(column=2, row=3, pady=6)

# image preview
canvas = Canvas(mainframe, width=300, height=300)      
canvas.grid(column=1, row=4, columnspan=3)     
img = Image.open("s.png")
# resize the image
resized_image = img.resize((300,300), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(10, 10, anchor=NW, image=new_image)  

# calculate button
# TODO command=
ttk.Button(mainframe, text="Calculate").grid(column=2, row=5, pady=12)

root.mainloop()