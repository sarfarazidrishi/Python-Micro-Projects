from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restart_with_time():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown -l")
    
def shutdown():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("shut down app")
st.geometry("500x300")
st.config(bg="light blue")

"""attibutes in font(("font name", font-size, font style),
hover effect over button, cursor , command is used to call function)"""
restart_btn=Button(st,text="Restart",font=("Time New Roman",15,"bold"),
                   relief="raised",cursor="plus", command=restart)
restart_btn.place(x=150, y=20, height=40, width=200)

restart_with_time=Button(st, text="Restart with time", font=("Time New Roman",15,"bold"),
                         relief="raised",cursor="plus", command=restart_with_time)
restart_with_time.place(x=150, y=80, height=40, width=200)

log_out=Button(st, text="Log out",font=("Time New Roman",15,"bold"),
               relief="raised",cursor="plus", command=logout)
log_out.place(x=150, y=140, height=40, width=200)

shut_down=Button(st, text="Shut down",font=("Time New Roman",15,"bold"),
                 relief="raised",cursor="plus", command=shutdown)
shut_down.place(x=150, y=200, height=40, width=200)

st.mainloop()