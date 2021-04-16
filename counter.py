import tkinter as tk
import time

root = tk.Tk()
cookie = tk.Label(text='Cookie', font=('Verdana', 40))
cookie.pack()
score = tk.Label(text='0', font=('Verdana', 40))
score.pack(side='bottom')
button = tk.Button(text='🧇', width=50, height=50, font=("Verdana",50))

i = 0

def addCount(event):
    global i
    i = i + 1
    print(i)
    score['text'] = i

button.bind('<Button-1>', addCount)
button.pack()


root.geometry('400x400')
root.title("Cookie")
root.mainloop()
