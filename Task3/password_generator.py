import tkinter as tk
import customtkinter as ct
import string
import random
import pyperclip
from tkinter import messagebox



uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
numbers = list(string.digits )
special_characters = ['!', '@', '#', '$', '%',  '&', '*', '(']
password=""
lenght = 0
com = ""
def generate_pass():
    if optionmenu.get() ==   'Password Complexity' :
        messagebox.showerror(title="Complexity not defined" , message="Make sure to set up the Complexity")
    else :
        global password
        global lenght
        password = ""
        lst = []
        if str(com) == ' Simple':
            for i in range(lenght):
                lst.extend(random.sample(numbers, k=1))
        elif com == ' Normal':
            for i in range(lenght):
                lst.extend(random.sample(numbers + lowercase_letters + uppercase_letters, k=1))
        elif com == ' Extreem':
            for i in range(lenght - 2):
                lst.extend(random.sample(numbers + lowercase_letters + uppercase_letters + special_characters, k=1))
            lst.extend(random.sample(special_characters, k=2))
            random.shuffle(lst)
        password = ''.join(lst)

        result.delete(0, tk.END)
        result.insert(0, password)

def slider_event(value):
    screen.configure(state="normal")
    value = int(value)
    screen.delete(0,tk.END)
    screen.insert(0,int(value))
    global lenght
    lenght = value
    screen.configure(state="disabled")


def optionmenu_callback(choice):
    global com
    com = choice


def copy_to_clipboard():
        text_to_copy = result.get()
        pyperclip.copy(text_to_copy)



app = ct.CTk()
app.title("Password Generator")
app.geometry("460x500")
app.resizable(False,False)
app.config(bg='#05121c')

font_title = ("Azonix" ,22 )
title=ct.CTkLabel(app , text="Welcome To\n Password Generator", text_color="#0080ff" ,font=font_title )
title.configure(bg_color='#05121c')
title.place(x=70 ,y= 20)

my_frame = ct.CTkFrame(app , width=430 , height=360 , fg_color="#3780c8")
my_frame.place(x=14,y=80)

line=ct.CTkLabel(app, text="Choose the length of the Password :" , font=("Azonix" ,13 , 'bold') , fg_color="#3780c8"  , bg_color='#3780c8')
line.place(x=65,y=90)


 # lenght
slider = ct.CTkSlider(app, from_=4, to=12, width=210 ,command=slider_event , number_of_steps =8 , hover=True ,bg_color="#3780c8")
slider.place(x=195, y =150)

box=ct.CTkLabel(app , text="4" , bg_color="#3780c8" , fg_color='#3780c8'  , font=("Azonix" ,17 , 'bold') , text_color="#000000"  )
box.place(x=176 , y=144)
box=ct.CTkLabel(app , text="12"   , bg_color="#3780c8" , fg_color='#3780c8'  , font=("Azonix" ,17 , 'bold') , text_color="#000000"  )
box.place(x=410 , y=144)

screen=ct.CTkEntry(app,textvariable="" , width=80 , height=40 , bg_color="#3780c8" , fg_color="#22282b"
                   ,placeholder_text="8", font=('Azonix',13) )
screen.place(x=40 , y =140 )
screen.configure(state="disabled")

# complexity



optionmenu = ct.CTkOptionMenu(app, values=[" Simple", " Normal" , " Extreem"],command=optionmenu_callback , bg_color="#3780c8" , width=150 , height=35 , fg_color='#26598c'
                              ,font=("Azonix" ,12) , dropdown_fg_color="#1b4064" , dropdown_font=("Azonix" ,11) ,dropdown_hover_color="#163350")

optionmenu.set(" Password Complexity ")
optionmenu.place(x=125,y=220)


#result

result_btn=ct.CTkButton(app,  text= "Generate" , width=180 , height=40 ,bg_color="#3780c8" , fg_color="#000000"
                        , font=("Azonix" ,15 ) ,text_color="#0080ff" , hover_color="#10263c" ,command=generate_pass  )
result_btn.place(x=30,y=300)

result=ct.CTkEntry(app,textvariable="" , width=180 , height=40 , bg_color="#3780c8" , fg_color="#22282b" ,placeholder_text="Empty"
                   , corner_radius=10 , border_width=3 ,border_color="#000000" , font=('Arial',17) )
result.place(x=250 , y =300 )

# copy

copy_btn=ct.CTkButton(app,  text= "Copy To My ClipBoard" , width=280 , height=40 ,bg_color="#3780c8" , fg_color="#000000"
                      , font=("Azonix" ,15 ) ,text_color="#0080ff" , hover_color="#10263c",command=copy_to_clipboard)
copy_btn.place(x=80,y=370)




app.mainloop()