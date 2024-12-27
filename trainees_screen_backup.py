from customtkinter import *
from PIL import Image, ImageTk
#import datetime as dt
#from arabic_datetime import ArabicDate
import sys
sys.path.append('.')
from custom_widgets.Buttons import *
from custom_widgets.Entries import *
from custom_widgets.Labels import *
from custom_widgets.Checkboxen import *
from custom_widgets.Frames import *
from custom_widgets.Combobox import *
from custom_widgets.SegmentedButton import *
# customtkinter.deactivate_automatic_dpi_awareness()
root = CTk()
root.state('zoomed')
root .geometry('1920x1080')
root.resizable(True, True)
root.title('')
set_appearance_mode('light')

trainees_name = Home_Frame(root, width = 1820, height = 960)
trainees_name.pack(padx = 50, pady = 150)

j = 5
for i in range (0, 20):
    label = Small_Label(trainees_name, fg_color = '#4F0000', text = 'سيف الدين أحمد محمد عبد الرحيم', text_color = 'white', font = ('Cairo Black', 15))
    label.grid(row = j, column = 0, padx = 1500, pady = 10)
    j += 1


root.mainloop()