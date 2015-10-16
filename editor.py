# Simple text editor using tkinter

import Tkinter as tk 
import tkFont

class Editor(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("text-editor-basic")

        self.textWindow = tk.Text(font="18")
        self.textWindow.pack(fill=tk.BOTH, expand=tk.YES)

        menubar = tk.Menu(self)

        formatmenu = tk.Menu(menubar)
        formatmenu.add_command(label='Increase font size', command = self.incFontSize)
        formatmenu.add_command(label='Decrease font size', command = self.decFontSize)
        menubar.add_cascade(label = 'Format', menu = formatmenu)

        self.parent.config(menu = menubar)

    def incFontSize(self):
        """ Increase editor font size by one unit."""
        font = tkFont.Font(font = self.textWindow['font'])
        font.config(size = str(int(font['size']+1)))
        self.textWindow.config(font=font)

    def decFontSize(self):
        """ Increase editor font size by one unit."""
        font = tkFont.Font(font = self.textWindow['font'])
        font.config(size = str(int(font['size']-1)))
        self.textWindow.config(font=font)

def main():
    root = tk.Tk()
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
