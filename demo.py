#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'

#--python2.x写法
# from Tkinter import *
# import tkMessageBox

#--python3.x写法
from tkinter import *
import tkinter.messagebox as tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Alert', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
