'''
project-name=GIF TO BOOT ANIMATION
DATE=30-01-2024
DEVLOPER=SHASHAN SONI
https://github.com/soni-shashan/
'''

from customtkinter import *
from tkinter import filedialog
import threading
import sys
import os
import shutil
import signal
import create_boot_animation

def goTo():
    if create_boot_animation.create(file_path,width,hight,fps,'OUTPUT'):
        os.remove('OUTPUT/desc.txt')
        shutil.rmtree('OUTPUT/part0')
        information.destroy()
        app.quit()
        
def click_sumbit():
    global width,hight,fps
    if width_entry.get()!="":
        width=width_entry.get()
        if not isinstance(width,int):
            width=int(width)
    else:
        width=1024
    if hight_entry.get()!="":
        hight=hight_entry.get()
        if not isinstance(hight,int):
            hight=int(hight)
    else:
        hight=600
    if fps_entry.get()!="":
        fps=fps_entry.get()
        if not isinstance(fps,int):
            fps=int(fps)
    else:
        fps=60

    global command,information,file_path
    file_path=file_path.replace("/","\\\\")
    command=f"{sys._MEIPASS}/python {sys._MEIPASS}/create_boot_animation.py \"{file_path}\" {width} {hight} {fps} output -zip"
    label.destroy()
    width_text.destroy()
    width_entry.destroy()
    hight_text.destroy()
    hight_entry.destroy()
    fps_label.destroy()
    fps_entry.destroy()
    create_btn.destroy()
    information=CTkLabel(app,text="Please wait!! it may take 5-10 seconds.",fg_color="transparent",font=('arial',16))
    information.place(relx=0.5,rely=0.5,anchor="center")
    therde=threading.Thread(target=goTo)
    therde.start()

def select_gif_file():
    global file_path,width_entry,hight_entry,fps_entry,label,width_text,hight_text,fps_entry,create_btn,fps_label
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    # Do something with the selected GIF file path (e.g., display it, process it, etc.)
    if file_path!="":
        print("Selected GIF file: ", file_path)
        btn.destroy()

        label = CTkLabel(app, text="Selected GIF file: "+ file_path, fg_color="transparent",font=('arial',14))
        label.place(relx=0.5, rely=0.1, anchor="center")

        width_text=CTkLabel(app,text="WIDTH (DEFUALT: 1024)",fg_color="transparent",font=('arial',16))
        width_text.place(relx=0.5,rely=0.15,anchor="center")

        width_entry=CTkEntry(app,width=170,text_color="#000000")
        width_entry.place(relx=0.5,rely=0.22,anchor="center")

        hight_text=CTkLabel(app,text="HIGHT (DEFUALT: 600)",fg_color="transparent",font=('arial',16))
        hight_text.place(relx=0.5,rely=0.3,anchor="center")

        hight_entry=CTkEntry(app,width=170,text_color="#000000")
        hight_entry.place(relx=0.5,rely=0.37,anchor="center")

        fps_label=CTkLabel(app,text="FPS (DEFUALT: 60)",fg_color="transparent",font=('arial',16))
        fps_label.place(relx=0.5,rely=0.45,anchor="center")

        fps_entry=CTkEntry(app,width=170,text_color="#000000")
        fps_entry.place(relx=0.5,rely=0.52,anchor="center")

        create_btn=CTkButton(master=app,text='CREATE',corner_radius=20,fg_color="#C850C0",hover_color="#4158D0",border_color="#000000",border_width=2,width=150,height=50,command=click_sumbit)
        create_btn.place(relx=0.5,rely=0.65,anchor="center")
        width_entry.focus_set()

def on_closing():
    os.kill(os.getpid(), signal.SIGINT)
    sys.exit()

if __name__=='__main__':
    app=CTk()
    app.geometry("512x512")
    app.minsize(512,512)
    app.maxsize(512,512)
    app.title('GIF TO BOOT ANIMATITON')
    app.protocol("WM_DELETE_WINDOW", on_closing)
    set_appearance_mode("light")
    app.iconbitmap(sys._MEIPASS+"\loading.ico")
    btn=CTkButton(master=app,text='Select Gif',corner_radius=20,fg_color="#C850C0",hover_color="#4158D0",border_color="#000000",border_width=2,width=150,height=50,command=select_gif_file)
    btn.place(relx=0.5,rely=0.1,anchor="center")
    app.mainloop()