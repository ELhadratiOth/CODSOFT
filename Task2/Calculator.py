import customtkinter as ct
from tkinter import messagebox

i=0
operation = ""
def display(value) :
    screen.configure(state="normal")
    global operation
    global i
    if len(operation) >= 2 and  len(operation) <=15 :

        if  value in ["*" , '/' ] and operation[-1] in  [ '/' , '*' ,'-' , '+' ] :
            messagebox.showerror(title="Syntax Error" , message="Try to make a valid Math expression")
            screen.delete(len(operation))

        else:
            operation += value
            screen.insert(i,operation[i])
            i+=1
    elif len(operation) >=6 :
        messagebox.showerror(title="Display Error", message="You surpass the limite of Calculator")

    else :
        operation +=value
        screen.insert(i,operation[i])
        i+=1
    screen.configure(state="disabled")


def button_clear():
    screen.configure(state="normal")
    global operation
    global i
    screen.delete(0,len(operation))
    operation = ""
    i=0
    screen.configure(placeholder_text="0")
    screen.configure(state="disabled")


def result():
    screen.configure(state="normal")
    try:
        screen.delete(0,len(operation))
        result = eval(operation)
        screen.insert(0,result)
    except Exception :
        messagebox.showerror(title="Math Error", message="Try to make a valid Logical Math expression")
    screen.configure(state="disabled")


def clear_1():
    screen.configure(state="normal")

    global operation

    global  i

    if len(operation) >=1 and i>=0 :
        recap = operation[:-1]
        operation = ""
        i=0
        screen.delete(0, len(recap)+1)
        for k in recap :
            display(k)
    screen.configure(state="disabled")


app = ct.CTk()
app.title("Calculator")
app.geometry("380x450")
app.resizable(False,False)
app.config(bg='#05121c')
font_title = ('Azonix', 25, 'bold')
label_titre=ct.CTkLabel(app,text="Calculator" ,   bg_color='#000033' , font=font_title )
label_titre.place(x=90, y=18)
screen = ct.CTkEntry(app, textvariable="",font=font_title ,placeholder_text="0"  ,bg_color='#000033' , corner_radius= 5,fg_color='#000000', border_color="#0e2e48" ,text_color=  '#ffffff' , width=380 , height=70  )
screen.place(x=0, y=60)
screen.configure(state="disabled")

#first line
font_btn = ('Azonix', 19)
font_btn_op = ('Azonix', 22)

button1 = ct.CTkButton(app, text="AC" ,font=font_btn, fg_color="#5D5E5B"  , hover_color="#0e2e48" ,command=button_clear ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button1.place(x=8 , y=140)
button2 = ct.CTkButton(app, text="DEL", font=font_btn, fg_color="#5D5E5B"  , hover_color="#0e2e48" ,command= clear_1 ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button2.place(x=101 , y=140)
button3 = ct.CTkButton(app, text="/", font=font_btn_op, fg_color="#015ea8"  , hover_color="#0e2e48" ,command=lambda : display('/') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button3.place(x=194 , y=140)
button4 = ct.CTkButton(app, text="x", font=font_btn, fg_color="#015ea8"  , hover_color="#0e2e48" ,command=lambda : display('*') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button4.place(x=287 , y=140)

#second line
button5 = ct.CTkButton(app, text="7", text_color='#015ea8' ,font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('7') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button5.place(x=8 , y=200)
button6 = ct.CTkButton(app, text="8",text_color='#015ea8' , font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('8') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button6.place(x=101 , y=200)
button7 = ct.CTkButton(app, text="9", text_color='#015ea8',font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('9') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button7.place(x=194 , y=200)
button8 = ct.CTkButton(app, text="-", font=font_btn_op, fg_color="#015ea8"  , hover_color="#0e2e48" ,  command=lambda : display('-') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button8.place(x=287 , y=200)

#third line
button9 = ct.CTkButton(app, text="4", text_color='#015ea8' ,font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('4') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button9.place(x=8 , y=260)
button10 = ct.CTkButton(app, text="5",text_color='#015ea8' , font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('5') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button10.place(x=101 , y=260)
button11 = ct.CTkButton(app, text="6", text_color='#015ea8',font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('6') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button11.place(x=194 , y=260)
button12 = ct.CTkButton(app, text="+", font=font_btn_op, fg_color="#015ea8"  , hover_color="#0e2e48" ,command=lambda : display('+') ,height=70,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button12.place(x=287 , y=260)

#fourth line
button13 = ct.CTkButton(app, text="1", text_color='#015ea8' ,font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('1') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button13.place(x=8 , y=320)
button14 = ct.CTkButton(app, text="2",text_color='#015ea8' , font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('2'),height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button14.place(x=101 , y=320)
button15 = ct.CTkButton(app, text="3", text_color='#015ea8',font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('3') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button15.place(x=194 , y=320)


#fifth line

button16 = ct.CTkButton(app, text="0", text_color='#015ea8' ,font=font_btn, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('0') ,height=40,width=168 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button16.place(x=8 , y=380)
button17 = ct.CTkButton(app, text=".",text_color='#015ea8' , font=font_btn_op, fg_color="#2D2E33"  , hover_color="#0e2e48" ,command=lambda : display('.') ,height=40,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button17.place(x=194 , y=380)
button18 = ct.CTkButton(app, text="=", font=font_btn_op, fg_color="#015ea8"  , hover_color="#0e2e48" ,command=result ,height=70,width=80 , bg_color='#000033' ,  border_color= "#000000"  ,border_width=2)
button18.place(x=287 , y=350)





app.mainloop()
