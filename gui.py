# preview i calculate se pozivaju
# preview ne radi provjera ako su brojevi upisani u entry, dunno y yet
# jos nisam zavrsio ih skroz al sa pushao da znas sta se poziva 

# libraries
from tkinter import *
from tkinter import ttk
# pip install Pillow
from PIL import Image, ImageTk

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

    print(cnt == 0)
    return cnt == 0

def preview():
    if not check_entry: return
    print('all numbers')

def calculate():
    pass


# window and title
root = Tk()
root.title("Rain amount")

# main frame and window config
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(340, 490)
root.maxsize(340, 490)

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

# preview button
ttk.Button(mainframe, text='Preview', command=preview).grid(column=2, row=3, pady=6)

# image preview
canvas = Canvas(mainframe, width=300, height=300)      
canvas.grid(column=1, row=4, columnspan=3)     
img = Image.open("s.png")
# resize the image
resized_image = img.resize((300,300), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(10, 10, image=new_image)  

# calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=5, pady=12)

value_headline_label = ttk.Label(mainframe, text='Amount of rain(L):')
value_headline_label.grid(column=2, row=6)
value_label = ttk.Label(mainframe, text='12 L')
value_label.grid(column=2, row=7)

root.mainloop()