from tkinter import *


class Notepad:
    __root = Tk()
    __thisTextArea = Text(__root, font=('Verdana', 30))
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar)
    __thisEditMenu = Menu(__thisMenuBar)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        # self.__thisWidth = kwargs['width']
        # self.__thisHeight = kwargs['height']
        self.__root.title("Безымянный")
        self.__root.geometry("500x500")
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky=N+E+S+W)
        self.__thisFileMenu.add_command(label="Новый", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Открыть", command= self.__openFile)
        self.__thisFileMenu.add_command(label="Сохранить", command=self.__saveFile)
        self.__thisFileMenu.add_command(label="Выйти", command=self.__quitProgram)
        self.__thisMenuBar.add_cascade(label="Файл", menu = self.__thisFileMenu)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        # todo добавить привязку scrollBar к FileMenu


    def __newFile(self):
        pass
    def __saveFile(self):
        pass
    def __openFile(self):
        pass
    def __quitProgram(self):
        self.__root.destroy()
    def run(self):
        self.__root.mainloop()



notepad = Notepad()
notepad.run()
