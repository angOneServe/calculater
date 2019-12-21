from tkinter import *
from threading import Thread

class Calculater(Tk):
    #属性定义
    s_width=None
    s_height=None
    wight=300
    height=300
    text="please input num"       #计算面板显示文字
    textCount=len(text)

    def __init__(self):
        super().__init__()
        self.s_width=self.winfo_screenwidth()
        self.s_height=self.winfo_screenheight()
        Thread(target=self._buildWwin).start()
    def _buildWwin(self):
        #创建主窗口
        self.win=Tk()
        self.win.title("计算器")
        self.win.geometry(f"{self.wight}x{self.height}+{int((self.s_width-self.wight)/2)}+{int((self.s_height-self.height)/2)}")
        self._addUi()
        Thread(target=self.InputText).start()


        #窗口循环
        self.win.mainloop()

    def _addUi(self):
        self.inputText=Label(master=self.win,bg="green",width=self.wight,height=4)
        self.inputText["text"]="111"
        print(self.inputText.keys())
        self.inputText.pack()

    def InputText(self):
        while True:
         self.inputText["text"]=input("11")

Calculater()





