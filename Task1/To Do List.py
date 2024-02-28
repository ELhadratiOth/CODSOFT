import customtkinter as ct
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import sqlite3 as db
from datetime import datetime
import os

#function used
object_task =""
detail_task =""
result=()

def get_time():
    time_cr = str(datetime.now().hour).zfill(2) + '-' + str(datetime.now().minute).zfill(2) + '-' + str(
        datetime.now().second).zfill(2)
    return  time_cr, str(datetime.now().date())


def verif_task_existance():
    conn = db.connect('todo_db.db')
    global result
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todo_table WHERE object = ?", (object_task,))
    result = cursor.fetchone()
    print(result)
    cursor.close()
    conn.close()

def get_task():
    global object_task
    global detail_task
    object_task = box_subject.get()
    detail_task = textbox.get("0.0", "end")
    conn = db.connect("todo_db.db")
    conn.execute(''' 
                CREATE TABLE IF NOT EXISTS todo_table (
                    id INTEGER PRIMARY KEY,
                    object VARCHAR(256),
                    detail TEXT,
                    date_cr VARCHAR(20),
                    time_cr VARCHAR(20)
                )
    ''')
    verif_task_existance()
    if result == None :
        if len(object_task) == 0 :
            messagebox.showerror(title="Subject Not Found" , message="Please  insert A subject of that task ")
        elif len(object_task) > 20 :
            messagebox.showinfo(title="Object Too Long" , message="Please make Your Subject More shorter ( 20 Caracters )")
        else :
            if  listbox.get(0) == "No Task exists" :
                listbox.delete(0)

            time_cr, date_cr = get_time()
            #sqlitepart
            conn.execute('''INSERT INTO todo_table (object, detail, date_cr, time_cr) VALUES (?, ?, ?, ?) ''',
                           (object_task, detail_task, date_cr, time_cr))
            conn.commit()
            conn.close()
            textbox.delete("0.0", "end")
            box_subject.delete(0,tk.END)
            listbox.insert(tk.END, object_task)
    else :
        messagebox.showerror(title="Object Occured" , message=" Try to change the Object name because it's already exists ")

def get_objects():
    try:
        conn = db.connect('todo_db.db')
        cursor = conn.cursor()

        cursor.execute("SELECT object FROM todo_table ")

        # Fetch the results
        rows = cursor.fetchall()
        listbox.delete(0, tk.END)
        for row in rows:
            listbox.insert(tk.END, row)

        cursor.close()
        conn.close()
    except db.OperationalError  :
        listbox.insert(tk.END, "No Task exists")
    try:
        if len(rows) == 0 :
            listbox.insert(tk.END, "No Task exists")
    except UnboundLocalError :
        pass

def remove_tasks():
    responce = messagebox.askokcancel(title="Remove All Tasks", message=" Are You sure ?")
    if responce == True :
        try :
            os.remove("todo_db.db")
            listbox.delete(0,tk.END)
            listbox.insert(tk.END, "No Task exists")

        except FileNotFoundError :
            messagebox.showinfo(title="0 Task ", message=" Sorry , There is no Tasks to Remove",)




def del_task():
    if  len(listbox.curselection()) != 0 and listbox.get(0) !=  "No Task exists" :
        object2del = listbox.get( listbox.curselection())
        conn = db.connect('todo_db.db')
        cursor = conn.cursor()
        if type(object2del) == tuple :
            cursor.execute("DELETE FROM todo_table WHERE object = ?", (object2del[0],) )
        else :
            cursor.execute("DELETE FROM todo_table WHERE object = ?", (object2del,))
        conn.commit()
        # Fetch the results
        listbox.delete(0, tk.END)
        cursor.close()
        conn.close()
        get_objects()
    else :
        messagebox.showerror(title="Task Not Selected" ,message="Please Select a Task to do This Operation if it exsists")



def display_detail_task():
        object2del = listbox.get( listbox.curselection())
        conn = db.connect('todo_db.db')
        cursor = conn.cursor()
        if type(object2del) == tuple :
            cursor.execute("SELECT * FROM todo_table WHERE object = ?  " ,(object2del[0],))
        else :
            cursor.execute("SELECT * FROM todo_table WHERE object = ?  " ,(object2del,))

        # Fetch the results
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return  rows[0]



def open_toplevel():
    if len(listbox.curselection()) != 0 and listbox.get(0) != "No Task exists":

        global toplevel_window
        if toplevel_window is None or not toplevel_window.winfo_exists():
                toplevel_window = ct.CTkToplevel(app)
                toplevel_window.config(bg='#00131a')
                toplevel_window.geometry("400x320")
                toplevel_window.resizable(False,False)
                design(display_detail_task())
                toplevel_window.title(display_detail_task()[1].upper())
                toplevel_window.focus()

        else:
                toplevel_window.focus()
    else :
        messagebox.showerror(title="Task Not Selected" ,message="Please Select a Task to do This Operation")
def design(task):
    frame_t=ct.CTkFrame(toplevel_window , width=374, height=294 , fg_color='#04252f' , bg_color='#00131a' )
    frame_t.place(x=13 , y =14 )
    titre1 = ct.CTkLabel(frame_t, text= "Object : " , font=('Azonix' , 17 , 'bold') ,   )
    titre1.place(x=9 , y=10)
    frame_subject = ct.CTkFrame(frame_t  , height=36 , width=240 , border_width = 2 ,fg_color = '#2a383c'  )
    frame_subject.place(x=120 , y=7)
    entry_object  = ct.CTkLabel(frame_subject , text=task[1] , font=('Azonix' , 17 , 'bold') , bg_color='#2a383c'  )
    entry_object.place( x=13 , y=5 )

    titre2 = ct.CTkLabel(frame_t, text="  Detail  :", font=('Azonix', 17, 'bold'), )
    titre2.place(x=135, y=57)

    entry_detail = ct.CTkTextbox(frame_t,  bg_color = '#04252f' ,fg_color = '#2a383c', font = ('Azonix', 15), border_width = 2 , height=147 , width=350 )
    if len(task[2]) > 1 :
        entry_detail.insert("0.0", task[2] )
    else :
        entry_detail.insert("0.0", "(Empty field) "  )

    entry_detail.configure(state="disabled")
    entry_detail.place(x=10, y=95)

    #time
    frame_d=ct.CTkFrame(frame_t , width=350, height=25 , fg_color='#2a383c' , bg_color = '#04252f'  )
    frame_d.place(x=10 , y =255 )
    text_d = (ct.CTkLabel(frame_d,  text= "Made it In : " + task[4]+" " + task[3] , font=('Azonix' , 13) ,width=340, height=21, fg_color='#2a383c', bg_color='#2a383c'))
    text_d.place(x=2, y=2)








#app
app = ct.CTk()
app.geometry("700x800")
app.title("To Do List")
app.config(bg='#00131a')
app.resizable(False,False)
#image insertion
frame_task = ct.CTkFrame(app , width=400 , height=57 , fg_color="#04252f" , bg_color="#00131a"  , border_width=2 , border_color='#5e7d87'  )
frame_task.place(x=270,y=68)

my_image = ct.CTkImage(light_image=Image.open("laptop.png"),
                                  dark_image=Image.open("laptop.png"),
                                  size=(150, 150))
image_label = ct.CTkLabel(app, image=my_image, text="" , bg_color="#00131a")
image_label.place(x=100 , y=20)
#title
title=ct.CTkLabel(app , text = ' Task Tracker \n Stay Organized and Productive !' , font=('Azonix' , 17 , 'bold') , text_color='#00e6e6' ,bg_color='#04252f' )
title.place(x=280 , y=80)





#frame2


frame_task = ct.CTkFrame(app , width=230 , height=35 , fg_color="#04252f" , bg_color="#00131a"  ,  border_width=2 , border_color='#5e7d87'   )
frame_task.place(x=406,y=210)
my_frame2 = ct.CTkFrame(app , width=320 , height=420 , fg_color="#04252f" , bg_color="#00131a" , border_width=2 , border_color='#5e7d87')
my_frame2.place(x=358,y=230)
task=ct.CTkLabel(app , text = '  Make Your task  ' , font=('Azonix' , 17 , 'bold') ,  width=225 ,text_color='#00e6e6' , fg_color='#04252f' , bg_color='#04252f'   )
task.place(x=408 , y=217)
#object
subject=ct.CTkLabel(my_frame2, text="Object :" , font=('Azonix' , 14 , 'bold') , text_color="#ffffff" )
subject.place(x=10, y=20)
box_subject = ct.CTkEntry(my_frame2 , textvariable="" , bg_color= '#04252f' , height=40 , width=300 , fg_color='#2a383c' , font=('Azonix' , 12)  )
box_subject.place(x=10, y=50)
#detail
detail=ct.CTkLabel(my_frame2, text="Detail :" , font=('Azonix' , 14 , 'bold') , text_color="#ffffff" )
detail.place(x=10, y=100)
textbox = ct.CTkTextbox(my_frame2 ,  bg_color= '#04252f' , height=200 , width=300 , fg_color='#2a383c' , font=('Azonix' , 12) , border_width  =2   )
textbox.place(x=10, y=130)

#button2
btn=ct.CTkButton(my_frame2 , text="ADD TASK" , font=('Azonix',17, 'bold') , text_color='#000000',  width=130 , height=40 , fg_color= "#00cccc" ,hover_color= "#008080"
                 ,border_width= 3 , border_color= "#000000" , bg_color='#04252f' , command=get_task)
btn.place(x=100 , y=350)

#frame1
frame_op = ct.CTkFrame(app , width=230 , height=35 , fg_color="#04252f" , bg_color="#00131a"  ,  border_width=2 , border_color='#5e7d87'   )
frame_op.place(x=66,y=210)

tasks_frame = ct.CTkFrame(app , width=320 , height=420 , fg_color="#04252f" , bg_color="#00131a" ,  border_width=2 , border_color='#5e7d87')
tasks_frame.place(x=20,y=230)

opt=ct.CTkLabel(app , text = ' List Of Tasks : ' , font=('Azonix' , 17 , 'bold') ,  width=225 ,text_color='#00e6e6' , fg_color='#04252f' , bg_color='#04252f'   )
opt.place(x=68 , y=217)
#lists of tasks
listbox = tk.Listbox(tasks_frame , width=24  , height=18 , font=('Azonix' , 15), background="#0a0e0f" ,highlightcolor="#5e7d87" , bd=3  , fg="#ffffff"
                     , selectforeground="#000000" ,selectbackground='#00e6e6' )


listbox.place(x=17 , y=40 )
ctk_textbox_scrollbar = ct.CTkScrollbar(tasks_frame, command=listbox.yview ,height=303 , fg_color='#0a0e0f' )
ctk_textbox_scrollbar.place(x=289 , y = 35)
listbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)
#get old tasks
get_objects()



#buttom1

btn_del=ct.CTkButton(tasks_frame , text="DISPLAY TASK" , font=('Azonix',15, 'bold') , text_color='#000000',  width=100 , height=40 , fg_color= "#00cccc" ,hover_color= "#008080"
                 ,border_width= 3 , border_color= "#000000" , bg_color='#04252f' , command=open_toplevel)
btn_del.place(x=13 , y=370)
toplevel_window = None

btn_dis=ct.CTkButton(tasks_frame , text="DELETE TASK" , font=('Azonix',15, 'bold') , text_color='#000000',  width=100 , height=40 , fg_color= "#00cccc" ,hover_color= "#008080"
                 ,border_width= 3 , border_color= "#000000" , bg_color='#04252f' , command=del_task)
btn_dis.place(x=165 , y=370)



# fram3

option_frame = ct.CTkFrame(app , width=660 , height=80 , fg_color="#04252f" , bg_color="#00131a" ,  border_width=2 , border_color='#5e7d87')
option_frame.place(x=20,y=670)


btn_op2=ct.CTkButton( option_frame, text="DELETE ALL TASK" , font=('Azonix',17, 'bold') , text_color='#000000',  width=250 , height=40 , fg_color= "#00cccc" ,hover_color= "#0000ff"
                 ,border_width= 3 , border_color= "#000000" , bg_color='#04252f' , command=remove_tasks)
btn_op2.place(x=37 , y=19)
btn_op3=ct.CTkButton(option_frame , text="EXIT" , font=('Azonix',17, 'bold') , text_color='#000000',  width=250 , height=40 , hover_color= "#ff0000" ,fg_color= "#00cccc"
                 ,border_width= 3 , border_color= "#000000" , bg_color='#04252f' , command=exit)
btn_op3.place(x=360 , y=19)




app.mainloop()




