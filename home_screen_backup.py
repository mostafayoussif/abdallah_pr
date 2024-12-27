from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
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
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('C:\\Users\\MostafaPC\\Python_projects\\Abdallah\\pr\\part\\gym0-83a26-firebase-adminsdk-sokxa-4305373246.json')

firebase_admin.initialize_app(cred,
{
    'databaseURL' : 'https://gym0-83a26-default-rtdb.firebaseio.com/'     
})


customtkinter.deactivate_automatic_dpi_awareness()
root = CTk()
root.state('zoomed')
root .geometry('1920x1080')
root.resizable(True, True)
root.title('')
set_appearance_mode('light') 


refresh = 1
def all_trainers():
    global refresh
    i = 0
    fitness_trainers_frame.place_forget()
    cardio_trainers_frame.place_forget()
    personal_trainers_frame .place_forget()
    body_building_trainers_frame.place_forget()
    trainees_frame.place_forget()
    feddback_frame.place_forget()
    trainees_name.pack_forget()
    trainers_name.grid(row = 0, column = 0, padx = 50, pady = 50)
    
    if i < refresh:
        print(i)
        get_all_trainers()

def all_trainees():
    fitness_trainers_frame.place_forget()
    cardio_trainers_frame.place_forget()
    personal_trainers_frame .place_forget()
    body_building_trainers_frame.place_forget()
    trainees_frame.place_forget()
    feddback_frame.place_forget()
    trainees_name.place_forget()
    trainers_name.grid_forget()
    trainees_name.pack(padx = 50, pady = 150)
    options_frame.place(relx = 0.5, y = 940, anchor = 'center')

def home():
    fitness_trainers_frame.place(x = 1500, y = 250)
    cardio_trainers_frame.place(x = 1500, y = 590)
    personal_trainers_frame.place(x = 1150, y = 250)
    body_building_trainers_frame.place(x = 1150, y = 590)
    trainees_frame.place(x = 700, y = 250)
    feddback_frame.place(x = 250, y = 250)
    trainers_name.grid_forget()
    trainees_name.pack_forget()
    options_frame.place_forget()

def add_more_trainers():
    add_trainer_frame.place(x = 50, y = 860)
    add_trainer_name.place(x = 0, y = 0)



home_screen = Full_Screen_Frame(root)
home_screen.place(x = 0, y = 0)
top_frame = Top_Frame(root)
top_frame.place(relx = 0.5, y = 50, anchor = 'center')
home_frame = Top_Button(top_frame, text =  'الرئيسية', command = home)
home_frame.place(x = 535, y = 0)
trainers = Top_Button(top_frame, text = 'المدربين', command = all_trainers)
trainers.place(x = 384, y = 0)
trainees = Top_Button(top_frame, text = 'المتدربين',command=all_trainees)
trainees.place(x = 233, y = 0)
fitness_trainers_frame = Home_Frame(root, width = 250, height = 175)
fitness_trainers_frame.place(x = 1500, y = 250)
cardio_trainers_frame = Home_Frame(root)
cardio_trainers_frame.place(x = 1500, y = 590)
personal_trainers_frame = Home_Frame(root)
personal_trainers_frame.place(x = 1150, y = 250)
body_building_trainers_frame = Home_Frame(root)
body_building_trainers_frame.place(x = 1150, y = 590)
trainees_frame = Home_Frame(root, height = 540, width = 300)
trainees_frame.place(x = 700, y = 250)
feddback_frame = Home_Frame(root, height = 540, width = 300)
feddback_frame.place(x = 250, y = 250)
trainers_name = Home_Frame(root, width = 1770, height = 700)
options_frame = Top_Frame(root)
add = Top_Button(options_frame, text = ' إضافة', command = add_more_trainers)
add.place(x = 535, y = 0)
delete = Top_Button(options_frame, text = 'حذف')
delete.place(x = 384, y = 0)
update = Top_Button(options_frame, text = 'تعديل')
update.place(x = 233, y = 0)
trainees_name = Home_Frame(root, width = 1820, height = 960)

add_trainer_frame = Top_Frame(root, width = 1820, fg_color = 'white')
add_trainer_name = Entry(add_trainer_frame)
#--- edit -----
edit_trainer_frame = Top_Frame(root,width = 1770)

edit_trainer_name = Entry(edit_trainer_frame, width = 400)
edit_trainer_name.grid(row = 0, column = 1, padx = 20)

edit_trainer_nowd = Entry(edit_trainer_frame, width = 30)
edit_trainer_nowd.grid(row = 0, column = 1, padx = 20)

edit_trainer_wt = Entry(edit_trainer_frame, width = 70)
edit_trainer_wt.grid(row = 0, column = 2, padx = 20)

edit_trainer_Mobile_phone = Entry(edit_trainer_frame, width = 120)
edit_trainer_Mobile_phone.grid(row = 0, column = 3, padx = 20)

edit_trainer_ex_t = CTkComboBox(edit_trainer_frame, width = 100)
edit_trainer_ex_t.grid(row = 0, column = 5, padx = 20)





j = 0
for i in range (0, 20):
    label = Small_Label(trainees_name, fg_color = '#4F0000', text = 'Ali Nagy', text_color = 'white', font = ('Cairo Black', 15))
    label.grid(row = j, column = 0, padx = 1500, pady = 10)
    j += 1

def get_name_by_click(d):
    name = d
    print(name)


def delete_trainer(trainer_name, tb, tu, td):
    deletion_confirmation = messagebox.askyesno('confirm_deletion', f'Do you want to delete {trainer_name} permanently?')
    if deletion_confirmation == 1:
        trainer_seletion = db.reference(f'members/trainers/{trainer_name}').delete()
        # trainers_name.pack_forget()
        tb.grid_forget()
        tu.grid_forget()
        td.grid_forget()
    else:
        pass

def update_trainer(t_name, trainer_gender, ex_type, dn, tow, mp, s):
    edit_trainer_frame.grid()



def get_all_trainers():
    j = 0
    button_numbera = 1
    data = db.reference('members/trainers').get()
    for trainer in data.keys():
        trainer_data = db.reference(f'members/trainers/{trainer}').get()
        data_frame = Data_Frame(trainers_name)
        data_frame.grid(row = j, pady = 10)

        name = Data_Label(data_frame, width = 400, text = trainer_data['Name'])
        name.grid(row = j, column = 0, padx = 30)
        
        et = Data_Label(data_frame, width = 150, text = trainer_data['Exercises type'])
        et.grid(row = j, column = 1, padx = 80)

        gender = Data_Label(data_frame, width = 150, text = trainer_data['Gender'])
        gender.grid(row = j, column = 2, padx = 0)

        nowd = Data_Label(data_frame, width = 80, text = trainer_data['NOWD'])
        nowd.grid(row = j, column = 3, padx = 20)

        wt = Data_Label(data_frame, width = 80, text = trainer_data['WT'])
        wt.grid(row = j, column = 4, padx = 20)

        mobile_phone = Data_Label(data_frame, width = 150, text = trainer_data['Mobile phone'])
        mobile_phone.grid(row = j, column = 5, padx = 20)

        status = Data_Label(data_frame, width = 120, text = trainer_data['Status'])
        status.grid(row = j, column = 6, padx = 20)
        

        update_trainer_button = Operation_Button(trainers_name, text = 'update',
                                                 command = lambda t_name = name, trainer_gender = gender, ex_type = et, dn = nowd, tow = wt, mp = mobile_phone, s = status: 
                                                 update_trainer(t_name, trainer_gender, ex_type, dn, tow, mp, s))
        update_trainer_button.grid(row = j, column = 1, padx = 10)
        delete_trainer_button = Operation_Button(trainers_name, text = 'delete',
                                                 command = lambda name = trainer, trainer_button = data_frame : delete_trainer(name, trainer_button))
        delete_trainer_button.configure(command = lambda name = trainer, trainer_data_button = data_frame, 
                                        trainer_update_button = update_trainer_button, trainer_delete_button = delete_trainer_button: delete_trainer(name, trainer_data_button, trainer_update_button, trainer_delete_button) )
        delete_trainer_button.grid(row = j, column = 2, padx = 5)
        j += 1





root.mainloop()