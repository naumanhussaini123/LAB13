from tkinter import*
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925*500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

img=PhotoImage(file='ai.jpg')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='blue')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('times new roman',23,'bold'))
heading.place(x=100,y=5)

user = Entry
root.mainloop()