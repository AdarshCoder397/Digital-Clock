from tkinter  import *
import time

clk = Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")
clk.config(bg="#0C1E28")

def clock():
    hr=str(time.strftime("%H"))
    mn=str(time.strftime("%M"))
    sc=str(time.strftime("%S"))
    # print(hr," : ",mn," : ",sc)
    if int(hr)>=12 and int(mn)>=0:
        nb.config(text="PM")
    if int(hr)>12:
        hr = str(int(int(hr)-12))
    hb.config(text=hr)
    mb.config(text=mn)
    sb.config(text=sc)

    hb.after(200,clock)

# Hours

hb = Label(clk,text="12",font=("Times 20 bold",75,'bold'),bg="#0875B7",fg="white")
hb.place(x=350,y=200,width=150,height=150)
hb_text = Label(clk,text="Hour",font=("Times 20 bold",20,"bold"),bg="#0875B7",fg="white")
hb_text.place(x=350,y=360,width=150,height=50)

# Minutes

mb = Label(clk,text="12",font=("Times 20 bold",75,'bold'),bg="#008EA4",fg="white")
mb.place(x=520,y=200,width=150,height=150)
mb_text = Label(clk,text="Minutes",font=("Times 20 bold",20,"bold"),bg="#008EA4",fg="white")
mb_text.place(x=520,y=360,width=150,height=50)

# Seconds

sb = Label(clk,text="12",font=("Times 20 bold",75,'bold'),bg="#06B4B8",fg="white")
sb.place(x=690,y=200,width=150,height=150)
sb_text = Label(clk,text="Seconds",font=("Times 20 bold",20,"bold"),bg="#06B4B8",fg="white")
sb_text.place(x=690,y=360,width=150,height=50)

# Time noon


nb = Label(clk,text="AM",font=("Times 20 bold",75,'bold'),bg="#9F0646",fg="white")
nb.place(x=860,y=200,width=172,height=150)
nb_text = Label(clk,text="Noon",font=("Times 20 bold",20,"bold"),bg="#9F0646",fg="white")
nb_text.place(x=860,y=360,width=172,height=50)

clock()
clk.mainloop()
