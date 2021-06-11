from tkinter import *
from tkinter import ttk
import subprocess

root=Tk()
root.title("Wireless Network Attack System")
root.geometry("750x750")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand = 1)

myCanvas = Canvas(main_frame)
myCanvas.pack(side=RIGHT, fill=BOTH, expand = 1)

myScrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=myCanvas.yview)
myScrollbar.pack( side = RIGHT, fill = Y )

myCanvas.configure(yscrollcommand=myScrollbar.set)
myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion = myCanvas.bbox("all")))
secondFrame = Frame(myCanvas)

myCanvas.create_window((0,0), window= secondFrame, anchor = "nw")

label=Label(secondFrame)

#ağ listesinin elde edilmesi
def agListeleme():
    # 
    devices = subprocess.check_output(['netsh','wlan','show','network','mode=bssid'])
    # decode it to strings
    devices = devices.decode('ascii')
    devices = devices.replace("\r","")
    label.pack()
    label.config(text=devices)

listeButton=Button(main_frame,text='Wifi Ağ Listesi', width=20 ,command=agListeleme)
listeButton.pack()






listeButton=Button(main_frame,text='Wifi Ağ Listesi', width=20 ,command=agListeleme)
listeButton.pack()


root.mainloop()

#rssi