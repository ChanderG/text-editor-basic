# Simple text editor using tkinter

import Tkinter as tk 
import tkFont
import tkMessageBox
import tkFileDialog

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

        # file menu 
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label='New', command = self.newFile)
        filemenu.add_command(label='Open', command = self.openFile)
        filemenu.add_command(label='Save', command = self.saveFile)
        menubar.add_cascade(label = 'File', menu=filemenu)

        formatmenu = tk.Menu(menubar)
        formatmenu.add_command(label='Increase font size', command = self.incFontSize)
        formatmenu.add_command(label='Decrease font size', command = self.decFontSize)
        formatmenu.add_command(label='Reverse colors', command = self.reverseColor)
        menubar.add_cascade(label = 'Format', menu = formatmenu)

        # help menus
        helpmenu = tk.Menu(menubar)
        helpmenu.add_command(label="About", command = self.displayAbout)
        menubar.add_cascade(label = "Help", menu = helpmenu)

        self.parent.config(menu = menubar)

    def newFile(self):
        """ Edit a new file. """
        if tkMessageBox.askyesno('Unsaved changes', 'Are you sure? You will lose unsaved changes!'):
            self.textWindow.delete("1.0", tk.END)

    def openFile(self):
        """ Open a new file for editing."""
        self.newFile()

        openedfile = tkFileDialog.askopenfile(mode='r')
        text = openedfile.read()
        self.textWindow.insert(tk.END, text)

    def saveFile(self):
        """ Save contents to a file.
        
        Simple brute force overwriting.
        """
        savefile = tkFileDialog.asksaveasfile(mode='w')
        text = self.textWindow.get("1.0", tk.END)
        savefile.write(text)
        savefile.close()

    def incFontSize(self):
        """ Increase editor font size by one unit."""
        font = tkFont.Font(font = self.textWindow['font'])
        font.config(size = str(int(font['size']+1)))
        self.textWindow.config(font=font)

    def decFontSize(self):
        """ Decrease editor font size by one unit."""
        font = tkFont.Font(font = self.textWindow['font'])
        font.config(size = str(int(font['size']-1)))
        self.textWindow.config(font=font)

    def reverseColor(self):
        """ Reverse color scheme. """
        fg_color = self.textWindow['foreground']
        bg_color = self.textWindow['background']

        # shows all config variables
        #print self.textWindow.config()
        # TODO -- take care of all variables, like highlight color, cursor color etc

        if fg_color == "#ffffff":
            self.textWindow.config(foreground="#000000")
        else:
            self.textWindow.config(foreground="#ffffff")

        if bg_color == "#ffffff":
            self.textWindow.config(background="#000000")
        else:
            self.textWindow.config(background="#ffffff")

    def displayAbout(self):
        """ Display an About message."""
        tkMessageBox.showinfo('About', "This is a basic text editor written for fun.")

def main():
    root = tk.Tk()
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
