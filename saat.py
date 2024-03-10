from tkinter import *
from tkinter.ttk import *
from time import strftime

saat_formatlari = {
    "12 saatlik": "%I:%M:%S %p",
    "24 saatlik": "%H:%M:%S"
}

saat_formati = saat_formatlari["24 saatlik"]

renkler = {
    "Siyah": "black",
    "Beyaz": "white",
    "Kirmizi": "red",
    "Mavi": "blue"
}

fontlar = {  
    "Arial": "Arial",
    "Courier New": "Courier New",
    "Times New Roman": "Times New Roman"
}

def set_font_size(event):
    width = saat.winfo_width()
    font_size = width // 15  # width'i 15'e bölelim, istediğiniz orana göre değiştirebilirsiniz.
    label.config(font=("Courier", font_size, "bold"))


saat = Tk()
saat.title("Saat ve Alarm")


frame = Frame(saat)
frame.pack(expand=True, fill=BOTH)


label = Label(frame, font="Courier 60 bold", background="black", foreground="cyan", anchor=CENTER)
label.pack(expand=True, fill=BOTH)

def time():
    global saat_formati
    string = strftime(saat_formati)
    label.config(text=string)
    label.after(1000, time)

def renk_secimi(event):
    renk = renkler[renk_menu.get()]
    label.config(background=renk)

renk_menu = Combobox(saat, values=list(renkler.keys()))
renk_menu.current(0)
renk_menu.bind("<<ComboboxSelected>>", renk_secimi)
renk_menu.pack()

def yazi_rengi_secimi(event):
    yazi_rengi = renkler[yazi_rengi_menu.get()]
    label.config(foreground=yazi_rengi)

yazi_rengi_menu = Combobox(saat, values=list(renkler.keys()))
yazi_rengi_menu.current(0)
yazi_rengi_menu.bind("<<ComboboxSelected>>", yazi_rengi_secimi)
yazi_rengi_menu.pack()

def font_secimi(event):
    font = fontlar[font_menu.get()]
    label.config(font=(font, 60, "bold"))

font_menu = Combobox(saat, values=list(fontlar.keys()))
font_menu.current(0)
font_menu.bind("<<ComboboxSelected>>", font_secimi)
font_menu.pack()


saat.bind("<Configure>", set_font_size)

time()
saat.mainloop()
