from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox, Notebook
from tkinter import Menu


def click():
    if combo.get()=='+':
        res=int(okno1.get())+int(okno2.get())
        lbl1.configure(text=str(res))
    elif combo.get() == '-':
        res = int(okno1.get()) - int(okno2.get())
        lbl1.configure(text=str(res))
    elif combo.get() == '*':
        res = int(okno1.get()) * int(okno2.get())
        lbl1.configure(text=str(res))
    elif combo.get() == ':':
        res = int(okno1.get()) / int(okno2.get())
        lbl1.configure(text=str(res))
def click2():
 lbl2.configure(text=selected.get())

w=Tk()
w.title('Чижов Никита Андреевич')
tab_control: Notebook=ttk.Notebook(w)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)

tab3=ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
tab_control.add(tab3, text='Третья')
okno1= Entry(tab1,width=6)
okno1.grid(column=0, row=0)
okno2 = Entry(tab1,width=6)
okno2.grid(column=3, row=0)
lbl1=Button(tab1, text="=",command=click,width=10)
lbl1.grid(column=4, row=0)
combo = Combobox(tab1)
combo['values'] = ('+','-','*',':')
combo.grid(column=1, row=0)

lbl2 = Label(tab2)
lbl2.grid(column=0, row=1)
selected = IntVar()
rad1 = Radiobutton(tab2,text='Первый', value=1,
variable=selected)
rad2 = Radiobutton(tab2,text='Второй', value=2,
variable=selected)
rad3 = Radiobutton(tab2,text='Третий', value=3,
variable=selected)
btn = Button(tab2, text="Клик", command=click2)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)







lbl3 = Label(tab3)
lbl3.grid(column=0, row=0)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", "end")
            text_editor.insert("1.0", text)


def save_file():
    filepath = fd.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", "end")
        with open(filepath, "w") as file:
            file.write(text)


text_editor = Text(tab3)
text_editor.grid(column=0, columnspan=2, row=1)
open_button = ttk.Button(tab3, text="Открыть файл", command=open_file)
open_button.grid(column=0, row=0, sticky='nsew', padx=10)
save_button = ttk.Button(tab3, text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=0, sticky='nsew', padx=10)





tab_control.pack(expand=1, fill='both')
w.mainloop()



