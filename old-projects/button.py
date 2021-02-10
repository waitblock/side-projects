import sys

import Tkinter
import tkMessageBox
#import Tkinter.tkMessageBox as mb

class App:
    def _init_(self, master):
        b=Button(master, text='Press Me', command=self.info).pack

tkMessageBox.showinfo("Title", "Please don't run this prpgram again!")
