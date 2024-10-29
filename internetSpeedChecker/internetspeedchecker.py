from tkinter import *
import speedtest

def speedcheck():
    spdtest=speedtest.Speedtest()
    spdtest.get_servers()
    down=str(round(spdtest.download()/(10**6), 3))+ "mbps"
    up=str(round(spdtest.upload()/(10**6), 3))+ "mbps"
    
    dn_speed_display.config(text=down)
    up_speed_display.config(text=up)
    
    
spdtest=Tk()
spdtest.title("Internet speed test")
spdtest.geometry("400x500")
spdtest.config(bg="yellow")


lab=Label(spdtest, text="internet speed test", font=("Times New Roman", 20, "bold"), background="black", fg="white")
lab.place(x=75, y=40, height=40, width=250)

dn_speed=Label(spdtest, text="Downloading Speed", font=("times new roman", 10, NORMAL), bg="Light blue", fg="black")
dn_speed.place(x=75, y=120,height=30, width=120)
dn_speed_display=Label(spdtest, text="00", font=("times new roman", 10, NORMAL), bg="white", fg="blue")
dn_speed_display.place(x=200, y=120,height=30, width=120)

up_speed=Label(spdtest, text="Uploading Speed", font=("times new roman", 10, NORMAL), bg="Light blue", fg="black")
up_speed.place(x=75, y=180,height=30, width=120)
up_speed_display=Label(spdtest, text="00", font=("times new roman", 10, NORMAL), bg="white", fg="blue")
up_speed_display.place(x=200, y=180,height=30, width=120)

button=Button(spdtest, text="check speed", font=("Times New Roman", 25, "bold"), relief=RAISED, command=speedcheck)
button.place(x=100, y=240, height=40, width=200)

spdtest.mainloop()
